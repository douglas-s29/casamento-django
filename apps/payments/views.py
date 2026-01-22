from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from apps.gifts.models import Gift
from .models import Payment

def process_payment(request, gift_id):
    """Process gift payment"""
    gift = get_object_or_404(Gift, pk=gift_id, is_active=True)
    
    if request.method == 'POST':
        # Validate quantity
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1 or quantity > 10:  # Reasonable limit
                return render(request, 'public/gifts.html', {
                    'error': 'Quantidade inválida. Escolha entre 1 e 10.'
                })
            if quantity > gift.available_quantity:
                return render(request, 'public/gifts.html', {
                    'error': 'Quantidade solicitada não disponível.'
                })
        except (ValueError, TypeError):
            return render(request, 'public/gifts.html', {
                'error': 'Quantidade inválida.'
            })
        
        # Create payment record
        payment = Payment.objects.create(
            gift=gift,
            buyer_name=request.POST.get('name', '').strip(),
            buyer_email=request.POST.get('email', '').strip(),
            buyer_phone=request.POST.get('phone', '').strip(),
            quantity=quantity,
            amount=gift.price * quantity,
            payment_method=request.POST.get('payment_method', 'pix'),
            message=request.POST.get('message', '').strip()
        )
        
        # TODO: Integrate with Asaas API
        # For now, just redirect to success
        return redirect('payments:success', payment_id=payment.id)
    
    return render(request, 'public/gifts.html', {'gift': gift})

def success(request, payment_id):
    """Payment success page"""
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, 'public/success.html', {'payment': payment})

@csrf_exempt
def webhook(request):
    """Asaas webhook handler"""
    # TODO: Implement Asaas webhook logic
    return JsonResponse({'status': 'ok'})
