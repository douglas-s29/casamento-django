from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['buyer_name', 'gift', 'amount', 'payment_method', 'status', 'created_at']
    list_filter = ['status', 'payment_method']
    search_fields = ['buyer_name', 'buyer_email']
    readonly_fields = ['created_at', 'updated_at', 'paid_at']
