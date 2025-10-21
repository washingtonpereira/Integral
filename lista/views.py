from django.shortcuts import render , redirect
from .models import Lista
from .forms import FormularioCadastro
from django.contrib.admin.views.decorators import staff_member_required


def home_list(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    if nome_filtrar:
        listas = Lista.objects.filter(nome__icontains=nome_filtrar)
    else:
        listas = Lista.objects.all()
    return render(request, 'lista/lista.html', {'listas': listas})

@staff_member_required
def cadastro(request):
    if request.method == 'POST':
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem')  
    else:
        form = FormularioCadastro()

    return render(request, 'lista/cadastro.html', {'form': form})

def index(request):
    return render(request,'lista/index.html')
     