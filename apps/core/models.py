from django.db import models


class EventSettings(models.Model):
    """Configurações do evento de casamento"""
    nome_noivo = models.CharField('Nome do Noivo', max_length=100)
    nome_noiva = models.CharField('Nome da Noiva', max_length=100)
    data_casamento = models.DateTimeField('Data e Hora do Casamento')
    local_nome = models.CharField('Nome do Local', max_length=200)
    local_endereco = models.TextField('Endereço Completo')
    local_latitude = models.DecimalField('Latitude', max_digits=9, decimal_places=6, null=True, blank=True)
    local_longitude = models.DecimalField('Longitude', max_digits=9, decimal_places=6, null=True, blank=True)
    local_maps_url = models.URLField('Link Google Maps', blank=True)
    local_waze_url = models.URLField('Link Waze', blank=True)
    mensagem_agradecimento = models.TextField('Mensagem de Agradecimento', default='Obrigado por nos presentear! ❤️')
    
    class Meta:
        verbose_name = 'Configuração do Evento'
        verbose_name_plural = 'Configurações do Evento'
    
    def __str__(self):
        return f"{self.nome_noivo} & {self.nome_noiva}"
    
    @classmethod
    def get_settings(cls):
        """Retorna as configurações do evento (singleton)"""
        return cls.objects.first()

