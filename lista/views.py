from django.shortcuts import render , redirect
from .models import Lista


def home_list(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    if nome_filtrar:
        listas = Lista.objects.filter(nome__icontains=nome_filtrar)
    else:
        listas = Lista.objects.all()
    return render(request, 'lista/lista.html', {'listas': listas})


def index(request):
    return render(request,'lista/index.html')
    