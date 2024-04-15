from django.contrib import admin

from .models import Despesa, Fornecedor


class DespesaAdmin(admin.ModelAdmin):
    
    list_display = ["data_despesa", "descricao_despesa", "nome_fornecedor", "valor_despesa"]
    list_filter = ["data_despesa"]
    search_fields = ["descricao_despesa"]

class FornecedorAdmin(admin.ModelAdmin):
    
    list_display = ["nome_fornecedor"]
    search_fields = ["descricao_despesa"]


admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
