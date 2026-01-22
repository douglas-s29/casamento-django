from django.db import models

class Gift(models.Model):
    """Gift registry item"""
    CATEGORY_CHOICES = [
        ('cozinha', 'Cozinha'),
        ('quarto', 'Quarto'),
        ('banheiro', 'Banheiro'),
        ('sala', 'Sala'),
        ('decoracao', 'Decoração'),
        ('outros', 'Outros'),
    ]
    
    name = models.CharField('Nome', max_length=200)
    description = models.TextField('Descrição')
    image = models.ImageField('Imagem', upload_to='gifts/')
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    category = models.CharField('Categoria', max_length=20, choices=CATEGORY_CHOICES, default='outros')
    total_quantity = models.PositiveIntegerField('Quantidade Total', default=1)
    purchased_quantity = models.PositiveIntegerField('Quantidade Comprada', default=0)
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Presente'
        verbose_name_plural = 'Presentes'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def available_quantity(self):
        return self.total_quantity - self.purchased_quantity

    @property
    def is_available(self):
        return self.is_active and self.available_quantity > 0

    @property
    def progress_percentage(self):
        if self.total_quantity == 0:
            return 0
        return int((self.purchased_quantity / self.total_quantity) * 100)
