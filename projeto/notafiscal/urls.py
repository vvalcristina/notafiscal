from django.urls import path
from projeto.notafiscal import views as v

app_name = 'notafiscal'

urlpatterns = [
    path('',v.notafiscal_list, name ='notafiscal_list'),
    path('<int:pk>/',v.notafiscal_detail, name ='notafiscal_detail'),
]
