from django.shortcuts import render
from passagens.forms import PassagemForms

def index(request):
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def minha_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        contexto = {'form':form}
        if form.is_valid():
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form Inválido')
            return render(request, 'index.html', contexto)