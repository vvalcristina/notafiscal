from django.urls import path
from empresa import views as v
from notafiscal import views

app_name = 'empresa'

urlpatterns = [
    path('', v.EmpresaList.as_view(), name='empresa_list'),
    path('',v.empresa_list, name='empresa_list'),
    path('<int:empresa>',views.notafiscal_list, name='notafiscal_list'),
    path('add/',v.EmpresaCreate.as_view(), name='empresa_add'),
    path('<int:pk>/edit/',v.EmpresaUpdate.as_view(), name='empresa_edit'),
]