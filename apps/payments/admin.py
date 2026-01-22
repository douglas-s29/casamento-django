from django.contrib import admin
from django.utils.html import format_html
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['asaas_payment_id', 'nome_comprador', 'presente', 'valor_total_display', 'quantidade', 'metodo_pagamento', 'status', 'data_criacao']
    list_filter = ['status', 'metodo_pagamento', 'data_criacao']
    search_fields = ['nome_comprador', 'email_comprador', 'asaas_payment_id']
    readonly_fields = ['asaas_payment_id', 'data_criacao', 'data_confirmacao', 'data_atualizacao']
    
    fieldsets = [
        ('Informações do Comprador', {
            'fields': ['nome_comprador', 'email_comprador', 'telefone_comprador']
        }),
        ('Informações do Presente', {
            'fields': ['presente', 'quantidade', 'valor']
        }),
        ('Informações do Pagamento', {
            'fields': ['asaas_payment_id', 'metodo_pagamento', 'status', 'link_pagamento']
        }),
        ('PIX', {
            'fields': ['qr_code', 'qr_code_image'],
            'classes': ['collapse']
        }),
        ('Datas', {
            'fields': ['data_criacao', 'data_confirmacao', 'data_atualizacao']
        }),
    ]
    
    def valor_total_display(self, obj):
        """Exibe o valor total formatado"""
        return f'R$ {obj.valor_total:.2f}'
    valor_total_display.short_description = 'Valor Total'
    
    def has_add_permission(self, request):
        # Pagamentos são criados apenas via site público
        return False

