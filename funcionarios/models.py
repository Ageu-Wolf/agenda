from django.db import models

from clientes.models import Pessoa


class Funcionario(Pessoa):
    funcao = models.CharField('Função', max_length=35 , help_text='Função na Empresa')
    data_admissao = models.DateField('Admissao', help_text='Data de admissão na empresa')


    class Meta:
        verbose_name= 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return super().nome
