from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Gift


def gift_list(request):
    """Lista de presentes disponíveis"""
    gifts = Gift.objects.filter(ativo=True).order_by('nome')
    context = {
        'gifts': gifts,
    }
    return render(request, 'public/gift_list.html', context)


def gift_detail(request, gift_id):
    """Detalhes de um presente"""
    gift = get_object_or_404(Gift, id=gift_id, ativo=True)
    
    if not gift.esta_disponivel:
        messages.warning(request, 'Este presente não está mais disponível.')
        return redirect('gifts:list')
    
    context = {
        'gift': gift,
    }
    return render(request, 'public/gift_detail.html', context)

