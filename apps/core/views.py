from django.shortcuts import render
from apps.core.models import EventSettings


def home(request):
    """Página inicial com contador regressivo"""
    event_settings = EventSettings.get_settings()
    context = {
        'event_settings': event_settings,
    }
    return render(request, 'public/home.html', context)


def venue(request):
    """Página com informações do local da cerimônia"""
    event_settings = EventSettings.get_settings()
    context = {
        'event_settings': event_settings,
    }
    return render(request, 'public/venue.html', context)

