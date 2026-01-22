from django.db import models
import uuid

class Guest(models.Model):
    """Guest/Invitee model"""
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmado'),
        ('declined', 'Não Pode Ir'),
    ]
    
    name = models.CharField('Nome', max_length=200)
    email = models.EmailField('E-mail', blank=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    unique_link = models.UUIDField('Link Único', default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField('Observações', blank=True)
    confirmed_at = models.DateTimeField('Confirmado em', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_rsvp_url(self):
        from django.urls import reverse
        return reverse('guests:rsvp', kwargs={'uuid': self.unique_link})
