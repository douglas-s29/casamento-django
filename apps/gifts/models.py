from django.db import models
from django.core.validators import MinValueValidator


class Gift(models.Model):
    """Modelo de presente"""
    nome = models.CharField('Nome', max_length=200)
    descricao = models.TextField('Descrição', blank=True)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    quantidade_total = models.PositiveIntegerField('Quantidade Total')
    quantidade_vendida = models.PositiveIntegerField('Quantidade Vendida', default=0)
    imagem = models.ImageField('Imagem', upload_to='gifts/', blank=True, null=True)
    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de Atualização', auto_now=True)
    
    class Meta:
        verbose_name = 'Presente'
        verbose_name_plural = 'Presentes'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    @property
    def quantidade_disponivel(self):
        """Retorna a quantidade disponível"""
        return self.quantidade_total - self.quantidade_vendida
    
    @property
    def esta_disponivel(self):
        """Verifica se o presente está disponível"""
        return self.ativo and self.quantidade_disponivel > 0
    
    def pode_vender(self, quantidade):
        """Verifica se é possível vender a quantidade solicitada"""
        return self.esta_disponivel and self.quantidade_disponivel >= quantidade

