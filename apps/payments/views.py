from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.utils import timezone
from .models import Payment
from apps.gifts.models import Gift
from apps.core.models import EventSettings
from .services import AsaasService
import json
from datetime import datetime, timedelta


def create_payment(request, gift_id):
    """Cria um pagamento para um presente"""
    gift = get_object_or_404(Gift, id=gift_id, ativo=True)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone', '')
        cpf = request.POST.get('cpf', '00000000000')
        metodo_pagamento = request.POST.get('metodo_pagamento')
        quantidade = int(request.POST.get('quantidade', 1))
        
        # Validação
        if not gift.pode_vender(quantidade):
            messages.error(request, 'Quantidade indisponível.')
            return redirect('gifts:detail', gift_id=gift.id)
        
        # Cria pagamento no Asaas
        asaas = AsaasService()
        
        customer_data = {
            'name': nome,
            'email': email,
            'cpfCnpj': cpf,
            'mobilePhone': telefone
        }
        
        valor_total = gift.valor * quantidade
        due_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        
        billing_type = 'PIX' if metodo_pagamento == 'PIX' else 'CREDIT_CARD'
        
        payment_data = {
            'billingType': billing_type,
            'value': float(valor_total),
            'dueDate': due_date,
            'description': f'Presente de Casamento - {gift.nome}',
            'externalReference': f'gift_{gift.id}',
        }
        
        result = asaas.create_payment(customer_data, payment_data)
        
        if 'error' in result or 'errors' in result:
            messages.error(request, 'Erro ao criar pagamento. Tente novamente.')
            return redirect('gifts:detail', gift_id=gift.id)
        
        # Salva o pagamento no banco de dados
        payment = Payment.objects.create(
            presente=gift,
            nome_comprador=nome,
            email_comprador=email,
            telefone_comprador=telefone,
            valor=gift.valor,
            quantidade=quantidade,
            asaas_payment_id=result['id'],
            status='pending',
            metodo_pagamento=metodo_pagamento,
            link_pagamento=result.get('invoiceUrl', ''),
        )
        
        # Se for PIX, busca o QR Code
        if metodo_pagamento == 'PIX':
            pix_data = asaas.get_pix_qrcode(result['id'])
            if not pix_data.get('error'):
                payment.qr_code = pix_data.get('payload', '')
                payment.qr_code_image = pix_data.get('encodedImage', '')
                payment.save()
        
        return redirect('payments:confirmation', payment_id=payment.id)
    
    context = {
        'gift': gift,
    }
    return render(request, 'public/payment_form.html', context)


def payment_confirmation(request, payment_id):
    """Página de confirmação do pagamento"""
    payment = get_object_or_404(Payment, id=payment_id)
    event_settings = EventSettings.get_settings()
    
    context = {
        'payment': payment,
        'event_settings': event_settings,
    }
    return render(request, 'public/payment_confirmation.html', context)


@csrf_exempt
def asaas_webhook(request):
    """Webhook para receber notificações do Asaas"""
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    # Valida o token do webhook
    token = request.headers.get('asaas-access-token') or request.GET.get('token')
    if token != settings.ASAAS_WEBHOOK_TOKEN:
        return HttpResponse(status=401)
    
    try:
        data = json.loads(request.body)
        event = data.get('event')
        payment_data = data.get('payment', {})
        payment_id = payment_data.get('id')
        
        if not payment_id:
            return HttpResponse(status=400)
        
        # Busca o pagamento no banco de dados
        try:
            payment = Payment.objects.get(asaas_payment_id=payment_id)
        except Payment.DoesNotExist:
            return HttpResponse(status=404)
        
        # Atualiza o status do pagamento
        if event == 'PAYMENT_CONFIRMED' or event == 'PAYMENT_RECEIVED':
            if payment.status != 'confirmed' and payment.status != 'received':
                payment.status = 'confirmed' if event == 'PAYMENT_CONFIRMED' else 'received'
                payment.data_confirmacao = timezone.now()
                payment.save()
                
                # Atualiza o estoque do presente
                gift = payment.presente
                gift.quantidade_vendida += payment.quantidade
                gift.save()
        
        elif event == 'PAYMENT_OVERDUE':
            payment.status = 'overdue'
            payment.save()
        
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)

