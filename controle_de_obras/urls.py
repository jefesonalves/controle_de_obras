from django.contrib import admin
from django.urls import path

from cadastro.views import DespesasListView, DespesasCreateView, DespesasUpdateView, DespesasDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DespesasListView.as_view(), name="despesas_list"),
    path('create', DespesasCreateView.as_view(), name="despesas_create"),
    path('update/<int:pk>', DespesasUpdateView.as_view(), name="despesas_update"),
    path('delete/<int:pk>', DespesasDeleteView.as_view(), name="despesas_delete"),
]

# Admin Site Config
admin.sites.AdminSite.site_header = 'Controle de Obras'