from django.contrib import admin
from .models import EventSettings

@admin.register(EventSettings)
class EventSettingsAdmin(admin.ModelAdmin):
    list_display = ['groom_name', 'bride_name', 'wedding_date']
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not EventSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
