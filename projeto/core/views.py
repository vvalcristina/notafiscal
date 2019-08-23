from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages

#Página inicial do sistema(Seja bem vindo...)
def index(request):
    return render(request, 'index.html')

#Login para add notas
def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    #Só pego por POST
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/login/#')
        else:
            messages.error(request,'Usuário e senha inválido. Favor tentar novamente')
    return redirect('/login/')
