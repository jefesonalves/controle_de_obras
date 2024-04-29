from django.db import models
from django.db.models import F

class Fornecedor(models.Model):
     nome_fornecedor = models.CharField(max_length=200, verbose_name='Fornecedor')

     class Meta:
        ordering = ["-pk"]
        verbose_name = 'Fornecedor'      
        verbose_name_plural = 'Fornecedores'

     def __str__(self):
           return f'{self.nome_fornecedor}'


class Despesa(models.Model):
    data_despesa = models.DateField(verbose_name='Data')
    descricao_despesa = models.CharField(max_length=200, verbose_name='Descrição')
    nome_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Fornecedor')
    quant_despesa = models.IntegerField(verbose_name='Quantidade')
    valor_despesa = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Valor Total')
    total_despesa = models.GeneratedField(
        expression = F("quant_despesa") * F("valor_despesa"), 
        output_field = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Valor Total'),
        db_persist=True,
    )

    class Meta:
        ordering = ["-data_despesa"] #Com o sinal de subtração fica em ordem descrescente
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        

    def __str__(self):
            return f'{self.descricao_despesa}'
