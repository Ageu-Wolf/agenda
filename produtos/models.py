from django.db import models
from django.db.models.functions import Upper

import fornecedores.models


class Produto(models.Model):
    nome = models.CharField('nome',max_length=50, help_text='Nome da produto', unique=True)
    preco = models.DecimalField('preço', max_digits=5, decimal_places=2, help_text='Preço do Produto')
    quantidade = models.DecimalField('quantidade',max_digits=5, decimal_places=2, help_text='Quantidade do Produto em estoque')
    fornecedor = models.ForeignKey(fornecedores.models.Fornecedor,verbose_name='Fornecedor', help_text='Nome do Fornecedor',
                                   on_delete=models.PROTECT, related_name='fornecedor')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = [Upper('nome')]
    def __str__(self):
        return self.nome