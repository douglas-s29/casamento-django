from django.db import models
import uuid


class Guest(models.Model):
    """Modelo de convidado"""
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('E-mail', blank=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    token_convite = models.UUIDField('Token do Convite', default=uuid.uuid4, unique=True, editable=False)
    confirmou_presenca = models.BooleanField('Confirmou Presença', null=True, blank=True)
    observacoes = models.TextField('Observações', blank=True)
    data_confirmacao = models.DateTimeField('Data da Confirmação', null=True, blank=True)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    def get_convite_url(self):
        """Retorna a URL do convite do convidado"""
        from django.urls import reverse
        return reverse('guests:convite', kwargs={'token': str(self.token_convite)})
    
    @property
    def status_confirmacao(self):
        """Retorna o status de confirmação"""
        if self.confirmou_presenca is None:
            return 'Pendente'
        elif self.confirmou_presenca:
            return 'Confirmado'
        else:
            return 'Não Confirmado'

