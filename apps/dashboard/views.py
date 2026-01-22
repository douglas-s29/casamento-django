from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from apps.guests.models import Guest
from apps.gifts.models import Gift
from apps.payments.models import Payment

@login_required
def dashboard(request):
    """Admin dashboard with statistics"""
    total_guests = Guest.objects.count()
    confirmed_guests = Guest.objects.filter(status='confirmed').count()
    total_revenue = Payment.objects.filter(status='confirmed').aggregate(Sum('amount'))['amount__sum'] or 0
    gifts_sold = Payment.objects.filter(status='confirmed').count()
    
    # Recent confirmations
    recent_confirmations = Guest.objects.filter(
        status__in=['confirmed', 'declined']
    ).order_by('-confirmed_at')[:5]
    
    # Recent payments
    recent_payments = Payment.objects.order_by('-created_at')[:5]
    
    # Days until wedding
    try:
        wedding_date = datetime.strptime(settings.WEDDING_DATE, '%Y-%m-%d %H:%M:%S')
        days_until = (wedding_date - datetime.now()).days
    except:
        days_until = 0
    
    context = {
        'total_guests': total_guests,
        'confirmed_guests': confirmed_guests,
        'total_revenue': total_revenue,
        'gifts_sold': gifts_sold,
        'recent_confirmations': recent_confirmations,
        'recent_payments': recent_payments,
        'days_until': days_until,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def guests_list(request):
    """List and manage guests"""
    guests = Guest.objects.all()
    return render(request, 'dashboard/guests.html', {'guests': guests})

@login_required
def gifts_list(request):
    """List and manage gifts"""
    gifts = Gift.objects.all()
    return render(request, 'dashboard/gifts_admin.html', {'gifts': gifts})

@login_required
def payments_list(request):
    """List and manage payments"""
    payments = Payment.objects.all()
    return render(request, 'dashboard/payments.html', {'payments': payments})

@login_required
def settings(request):
    """Event settings"""
    return render(request, 'dashboard/settings.html')
