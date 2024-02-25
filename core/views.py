from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        # print(f'Post:{request.POST}')
        if form.is_valid():
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']

            # print('Mensagem Enviada')
            # print(f'Nome: {nome}')
            # print(f'Email:{email}')
            # print(f'Assunto:{assunto}')
            # print(f'Mensagem:{mensagem}')

            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context ={
        'form': form
    }
    
    return render(request,'contato.html', context)

def produto(request):

    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            # prod = form.save(commit=False) # Não Consiste no db

            # print(f'Nome: {prod.nome}')
            # print(f'preco: {prod.preco}')
            # print(f'estoque: {prod.estoque}')
            # print(f'Imagem: {prod.imagem}')

            form.save()

            messages.success(request, 'Produto Salvo com Sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Error ao Salvar o Produto')
    else:
        form = ProdutoModelForm() 
    context = {'form': form}

    return render(request, 'produto.html', context)