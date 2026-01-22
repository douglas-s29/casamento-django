from django.contrib import admin
from .models import EventSettings


@admin.register(EventSettings)
class EventSettingsAdmin(admin.ModelAdmin):
    list_display = ['nome_noivo', 'nome_noiva', 'data_casamento', 'local_nome']
    fieldsets = [
        ('Informações dos Noivos', {
            'fields': ['nome_noivo', 'nome_noiva', 'data_casamento']
        }),
        ('Local do Evento', {
            'fields': ['local_nome', 'local_endereco', 'local_latitude', 'local_longitude', 'local_maps_url', 'local_waze_url']
        }),
        ('Mensagens', {
            'fields': ['mensagem_agradecimento']
        }),
    ]
    
    def has_add_permission(self, request):
        # Permite apenas uma instância de configuração
        return not EventSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Impede a exclusão da configuração
        return False

