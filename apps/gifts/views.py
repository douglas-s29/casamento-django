from django.shortcuts import render
from .models import Gift

def gift_list(request):
    """Gift registry list"""
    gifts = Gift.objects.filter(is_active=True)
    category = request.GET.get('category')
    
    if category:
        gifts = gifts.filter(category=category)
    
    return render(request, 'public/gifts.html', {
        'gifts': gifts,
        'selected_category': category
    })
