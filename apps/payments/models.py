from django.db import models
from django.core.validators import MinValueValidator
from apps.gifts.models import Gift


class Payment(models.Model):
    """Modelo de pagamento"""
    
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmado'),
        ('received', 'Recebido'),
        ('overdue', 'Vencido'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('PIX', 'PIX'),
        ('CREDIT_CARD', 'Cartão de Crédito'),
        ('BOLETO', 'Boleto'),
    ]
    
    presente = models.ForeignKey(Gift, on_delete=models.PROTECT, verbose_name='Presente')
    nome_comprador = models.CharField('Nome do Comprador', max_length=200)
    email_comprador = models.EmailField('E-mail do Comprador')
    telefone_comprador = models.CharField('Telefone do Comprador', max_length=20, blank=True)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    
    asaas_payment_id = models.CharField('ID do Pagamento Asaas', max_length=100, unique=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pending')
    metodo_pagamento = models.CharField('Método de Pagamento', max_length=20, choices=PAYMENT_METHOD_CHOICES)
    
    qr_code = models.TextField('QR Code PIX', blank=True)
    qr_code_image = models.URLField('Imagem QR Code', blank=True)
    link_pagamento = models.URLField('Link de Pagamento')
    
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    data_confirmacao = models.DateTimeField('Data de Confirmação', null=True, blank=True)
    data_atualizacao = models.DateTimeField('Data de Atualização', auto_now=True)
    
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return f"{self.nome_comprador} - {self.presente.nome} - R$ {self.valor}"
    
    @property
    def valor_total(self):
        """Retorna o valor total do pagamento"""
        return self.valor * self.quantidade

