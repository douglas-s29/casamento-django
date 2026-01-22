from django.contrib import admin
from .models import Gift

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'purchased_quantity', 'total_quantity', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
