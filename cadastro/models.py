from django.db import models

class Fornecedor(models.Model):
     nome_fornecedor = models.CharField(max_length=200, verbose_name='Fornecedor')

     class Meta:
        verbose_name = 'Fornecedors'
        verbose_name_plural = 'Fornecedores'

     def __str__(self):
           return f'{self.nome_fornecedor}'


class Despesa(models.Model):
    data_despesa = models.DateField(verbose_name='Data')
    descricao_despesa = models.CharField(max_length=200, verbose_name='Descrição')
    nome_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Fornecedor')
    # fornecedor = models.CharField("Fornecedor", max_length=200)
    valor_despesa = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor')

    class Meta:
        verbose_name = 'Despesas'
        verbose_name_plural = 'Despesas'


    def __str__(self):
            return f'{self.data_despesa}, {self.descricao_despesa}, {self.nome_fornecedor}, {self.valor_despesa}'
