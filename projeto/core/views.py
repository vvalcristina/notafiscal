from django.shortcuts import render
#Página inicial do sistema(Seja bem vindo...)

def index(request):
    return render(request, 'index.html')
