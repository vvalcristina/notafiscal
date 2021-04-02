from django.urls import path
from notafiscal import views as v

app_name = 'notafiscal'

urlpatterns = [
    path('', v.NotaFiscalList.as_view(), name='notafiscal_list'),
    path('<int:empresa>',v.notafiscal_list, name ='notafiscal_list'),
    path('<int:pk>/',v.notafiscal_detail, name ='notafiscal_detail'),
    path('add/',v.NotaFiscalCreate.as_view(), name ='notafiscal_add'),
    path('<int:pk>/edit/',v.NotaFiscalUpdate.as_view(), name ='notafiscal_edit'),
]