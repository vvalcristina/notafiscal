from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView

def index(request):
    return render(request, 'index.html')