from django.db import models

class EventSettings(models.Model):
    """Single row configuration for wedding event"""
    groom_name = models.CharField('Nome do Noivo', max_length=100)
    bride_name = models.CharField('Nome da Noiva', max_length=100)
    wedding_date = models.DateTimeField('Data do Casamento')
    ceremony_location_name = models.CharField('Nome do Local', max_length=200)
    ceremony_location_address = models.TextField('Endereço Completo')
    ceremony_location_lat = models.DecimalField('Latitude', max_digits=9, decimal_places=6, null=True, blank=True)
    ceremony_location_lng = models.DecimalField('Longitude', max_digits=9, decimal_places=6, null=True, blank=True)
    party_location_name = models.CharField('Nome do Local da Festa', max_length=200, blank=True)
    party_location_address = models.TextField('Endereço da Festa', blank=True)
    hero_image = models.ImageField('Imagem Hero', upload_to='hero/', null=True, blank=True)
    thank_you_message = models.TextField('Mensagem de Agradecimento', default='Obrigado por fazer parte do nosso dia especial!')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Configuração do Evento'
        verbose_name_plural = 'Configurações do Evento'

    def __str__(self):
        return f"{self.groom_name} & {self.bride_name}"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and EventSettings.objects.exists():
            raise ValueError('Only one EventSettings instance is allowed')
        return super().save(*args, **kwargs)
