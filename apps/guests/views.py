from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Guest


def convite(request, token):
    """Página de convite individual do convidado"""
    guest = get_object_or_404(Guest, token_convite=token)
    
    if request.method == 'POST':
        confirmou = request.POST.get('confirmou_presenca')
        observacoes = request.POST.get('observacoes', '')
        
        if confirmou == 'sim':
            guest.confirmou_presenca = True
            messages.success(request, 'Presença confirmada com sucesso! ❤️')
        elif confirmou == 'nao':
            guest.confirmou_presenca = False
            messages.info(request, 'Obrigado por nos avisar.')
        
        guest.observacoes = observacoes
        guest.data_confirmacao = timezone.now()
        guest.save()
        
        return redirect('guests:convite', token=token)
    
    context = {
        'guest': guest,
    }
    return render(request, 'public/convite.html', context)

