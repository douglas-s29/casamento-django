from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Guest

def rsvp(request, uuid):
    """RSVP confirmation page"""
    guest = get_object_or_404(Guest, unique_link=uuid)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        notes = request.POST.get('notes', '')
        
        guest.status = status
        guest.notes = notes
        if status == 'confirmed':
            guest.confirmed_at = timezone.now()
        guest.save()
        
        return render(request, 'public/rsvp.html', {
            'guest': guest,
            'success': True
        })
    
    return render(request, 'public/rsvp.html', {'guest': guest})
