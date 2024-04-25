from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Despesa

class DespesasListView(ListView):
    model = Despesa
    
class DespesasCreateView(CreateView):
    model = Despesa
    # fields = ["descricao_despesa"]
    fields = ["data_despesa", "descricao_despesa", "nome_fornecedor", "quant_despesa", "valor_despesa"]
    success_url = reverse_lazy("despesas_list")

class DespesasUpdateView(UpdateView):
    model = Despesa
    fields = ["descricao_despesa"]
    #fields = ["data_despesa", "descricao_despesa", "nome_fornecedor", "quant_despesa", "valor_despesa"]
    success_url = reverse_lazy("despesas_list")

class DespesasDeleteView(DeleteView):
    model = Despesa
    success_url = reverse_lazy("despesas_list")