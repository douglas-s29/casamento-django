from django.db import models
from apps.gifts.models import Gift

class Payment(models.Model):
    """Payment transactions"""
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmado'),
        ('received', 'Recebido'),
        ('cancelled', 'Cancelado'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('pix', 'PIX'),
        ('credit_card', 'Cartão de Crédito'),
    ]
    
    gift = models.ForeignKey(Gift, on_delete=models.PROTECT, verbose_name='Presente')
    buyer_name = models.CharField('Nome do Comprador', max_length=200)
    buyer_email = models.EmailField('E-mail')
    buyer_phone = models.CharField('Telefone', max_length=20, blank=True)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    amount = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    payment_method = models.CharField('Método de Pagamento', max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pending')
    message = models.TextField('Mensagem para os Noivos', blank=True)
    
    # Asaas integration fields
    asaas_payment_id = models.CharField('Asaas Payment ID', max_length=100, blank=True)
    asaas_invoice_url = models.URLField('URL da Fatura', blank=True)
    pix_qr_code = models.TextField('PIX QR Code', blank=True)
    pix_copy_paste = models.TextField('PIX Copia e Cola', blank=True)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    paid_at = models.DateTimeField('Pago em', null=True, blank=True)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.buyer_name} - {self.gift.name} - R$ {self.amount}"
