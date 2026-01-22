from django.contrib import admin
from django.utils.html import format_html
from .models import Gift


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'quantidade_total', 'quantidade_vendida', 'quantidade_disponivel_display', 'ativo', 'preview_imagem']
    list_filter = ['ativo', 'data_criacao']
    search_fields = ['nome', 'descricao']
    readonly_fields = ['quantidade_vendida', 'data_criacao', 'data_atualizacao', 'preview_imagem']
    
    fieldsets = [
        ('Informações do Presente', {
            'fields': ['nome', 'descricao', 'imagem', 'preview_imagem']
        }),
        ('Preço e Estoque', {
            'fields': ['valor', 'quantidade_total', 'quantidade_vendida']
        }),
        ('Status', {
            'fields': ['ativo']
        }),
    ]
    
    def quantidade_disponivel_display(self, obj):
        """Exibe quantidade disponível com cores"""
        disponivel = obj.quantidade_disponivel
        if disponivel == 0:
            color = 'red'
        elif disponivel < 3:
            color = 'orange'
        else:
            color = 'green'
        return format_html('<span style="color: {};">{}</span>', color, disponivel)
    quantidade_disponivel_display.short_description = 'Disponível'
    
    def preview_imagem(self, obj):
        """Exibe preview da imagem"""
        if obj.imagem:
            return format_html('<img src="{}" style="max-height: 200px;" />', obj.imagem.url)
        return '-'
    preview_imagem.short_description = 'Preview'

