from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from apps.guests.models import Guest
from apps.gifts.models import Gift
from apps.payments.models import Payment


@login_required
def dashboard(request):
    """Dashboard administrativo com estatísticas"""
    
    # Estatísticas de convidados
    total_convidados = Guest.objects.count()
    confirmados = Guest.objects.filter(confirmou_presenca=True).count()
    nao_confirmados = Guest.objects.filter(confirmou_presenca=False).count()
    pendentes = Guest.objects.filter(confirmou_presenca__isnull=True).count()
    
    # Estatísticas de presentes
    total_presentes = Gift.objects.count()
    presentes_disponiveis = Gift.objects.filter(ativo=True).count()
    
    # Estatísticas de pagamentos
    total_pagamentos = Payment.objects.count()
    pagamentos_confirmados = Payment.objects.filter(
        Q(status='confirmed') | Q(status='received')
    ).count()
    
    total_arrecadado = Payment.objects.filter(
        Q(status='confirmed') | Q(status='received')
    ).aggregate(total=Sum('valor'))['total'] or 0
    
    # Pagamentos recentes
    pagamentos_recentes = Payment.objects.select_related('presente').order_by('-data_criacao')[:10]
    
    # Presentes mais vendidos
    presentes_vendidos = Gift.objects.filter(quantidade_vendida__gt=0).order_by('-quantidade_vendida')[:5]
    
    context = {
        'total_convidados': total_convidados,
        'confirmados': confirmados,
        'nao_confirmados': nao_confirmados,
        'pendentes': pendentes,
        'total_presentes': total_presentes,
        'presentes_disponiveis': presentes_disponiveis,
        'total_pagamentos': total_pagamentos,
        'pagamentos_confirmados': pagamentos_confirmados,
        'total_arrecadado': total_arrecadado,
        'pagamentos_recentes': pagamentos_recentes,
        'presentes_vendidos': presentes_vendidos,
    }
    
    return render(request, 'admin/dashboard.html', context)

