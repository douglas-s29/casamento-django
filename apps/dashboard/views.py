from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
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
    
    context = {
        'total_guests': total_guests,
        'confirmed_guests': confirmed_guests,
        'total_revenue': total_revenue,
        'gifts_sold': gifts_sold,
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
