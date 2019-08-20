from django.urls import path
from projeto.empresa import views as v

app_name = 'empresa'

urlpatterns = [
    path('',v.empresa_list, name='empresa_list'),
    path('<int:pk>',v.empresa_detail, name='empresa_detail'),
    path('add/',v.EmpresaCreate.as_view(), name='empresa_add'),



]
