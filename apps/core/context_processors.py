from django.conf import settings
from .models import EventSettings

def wedding_context(request):
    """Add wedding settings to all templates"""
    context = {
        'GROOM_NAME': settings.WEDDING_GROOM_NAME,
        'BRIDE_NAME': settings.WEDDING_BRIDE_NAME,
        'WEDDING_DATE': settings.WEDDING_DATE,
    }
    
    # Try to get from database
    try:
        event = EventSettings.objects.first()
        if event:
            context.update({
                'GROOM_NAME': event.groom_name,
                'BRIDE_NAME': event.bride_name,
                'WEDDING_DATE': event.wedding_date,
                'event_settings': event,
            })
    except:
        pass
    
    return context
