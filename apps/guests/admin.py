from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'status_confirmacao', 'data_confirmacao', 'link_convite']
    list_filter = ['confirmou_presenca', 'data_criacao']
    search_fields = ['nome', 'email', 'telefone']
    readonly_fields = ['token_convite', 'data_criacao', 'link_convite_completo']
    
    fieldsets = [
        ('Informações do Convidado', {
            'fields': ['nome', 'email', 'telefone']
        }),
        ('Convite', {
            'fields': ['token_convite', 'link_convite_completo']
        }),
        ('Confirmação de Presença', {
            'fields': ['confirmou_presenca', 'data_confirmacao', 'observacoes']
        }),
    ]
    
    def link_convite(self, obj):
        """Exibe link do convite na lista"""
        url = obj.get_convite_url()
        return format_html('<a href="{}" target="_blank">Ver Convite</a>', url)
    link_convite.short_description = 'Link do Convite'
    
    def link_convite_completo(self, obj):
        """Exibe link completo do convite"""
        if obj.token_convite:
            url = obj.get_convite_url()
            full_url = f"http://localhost:8000{url}"
            return format_html('<a href="{}" target="_blank">{}</a>', full_url, full_url)
        return '-'
    link_convite_completo.short_description = 'Link Completo do Convite'

