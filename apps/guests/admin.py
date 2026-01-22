from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status', 'confirmed_at', 'created_at']
    list_filter = ['status']
    search_fields = ['name', 'email']
    readonly_fields = ['unique_link', 'confirmed_at', 'created_at', 'updated_at']
