from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Viagem, Categoria
from .forms.categoria_form import CategoriaForm
from .forms.viagem_form import ViagemForm
from django.contrib import messages
import requests


def sidebar(request):
    is_adm = request.user.groups.filter(name='ADM').exists()
    is_cliente = request.user.groups.filter(name='Cliente').exists()
    return {'is_adm': is_adm, 'is_cliente': is_cliente}


def criar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect('trip:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'trip/categoria/criar_categoria.html',
                  {'form': form})


def listar_categorias(request):
    categorias = Categoria.objects.all().order_by('-id')
    return render(request, 'trip/categoria/listar_categorias.html', {'categorias': categorias, **sidebar(request)})


def atualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso.')
            return redirect('trip:listar_categorias')

    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'trip/categoria/listar_categorias.html',
                  {'form': form, 'categoria': categoria, **sidebar(request)})


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        categoria.delete()
        messages.success(request, 'Categoria deletada com sucesso.')
        return redirect('trip:listar_categorias')

    return render(request, 'trip/categoria/listar_categorias.html',
                  {'categoria': categoria, **sidebar(request)})


def criar_viagem(request):

    if request.method == "POST":
        post_data = request.POST.copy()
        post_data['custo'] = post_data['custo'].replace(',', '.')
        post_data['preco'] = post_data['preco'].replace(',', '.')

        form = ViagemForm(post_data)

        if form.is_valid():
            form.save()
            messages.success(request, "Viagem cadastrada com sucesso!")
            return redirect('trip:listar_viagens')
    else:
        form = ViagemForm()
    return render(request, 'trip/viagem/criar_viagem.html', {'form': form, **sidebar(request)})


def listar_viagens(request):
    viagens = Viagem.objects.all().order_by('-id')
    categorias = Categoria.objects.filter(is_active=True).order_by('-id')
    return render(request, 'trip/viagem/listar_viagens.html',
                  {'viagens': viagens, 'categorias': categorias, ** sidebar(request)})


def atualizar_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)

    if request.method == "POST":
        post_data = request.POST.copy()
        post_data['custo'] = post_data['custo'].replace(',', '.')
        post_data['preco'] = post_data['preco'].replace(',', '.')
        form = ViagemForm(post_data, instance=viagem)
        if form.is_valid():
            form.save()
            messages.success(request, "Viagem atualizada com sucesso!")
            return redirect('trip:listar_viagens')
    else:
        form = ViagemForm(instance=viagem)

    return render(request, 'trip/viagem/listar_viagens.html',
                  {'form': form, 'viagem': viagem, **sidebar(request)})


def excluir_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)

    if request.method == "POST":
        viagem.delete()
        messages.success(request, "Viagem deletada com sucesso!")
        return redirect('trip:listar_viagens')

    return render(request, 'trip/viagem/listar_viagens.html',
                  {'viagem': viagem, **sidebar(request)})


def listar_viagens_disponiveis(request):
    # Filtra as viagens que estão ativas e têm vagas disponíveis
    viagens_disponiveis = Viagem.objects.filter(
        is_active=True, vagas_disponiveis__gt=0)

    return render(request, 'home.html', {'viagens_disponiveis': viagens_disponiveis})


def pagamento(request):
    # Dados necessários para criar o checkout
    dados_checkout = {
        "reference_id": "REF123",
        "items": [
            {
                "name": "Item de Teste2",
                "description": "Descrição do Item",
                "unit_amount": 50000,
                "quantity": 1
            }
        ],
        "sender": {
            "name": "Cliente Teste",
            "email": "cliente@teste.com"
        }
    }

    # URL da API do PagSeguro para criar um checkout
    url_api_pagseguro = 'https://sandbox.api.pagseguro.com/checkouts'

    # Autenticação na API do PagSeguro (substitua pelo seu email e token)
    token = '330222910B9B478094716615805DB373'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'

    }

    # Fazendo a requisição POST para criar o checkout
    # Fazendo com base na requisição feita via POSTMAN
    response = requests.post(
        url_api_pagseguro, json=dados_checkout, headers=headers)

    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200 or response.status_code == 201:
        # Obtém os dados do checkout da resposta da API
        # Primeiro mandamos um Body e recebemos outro
        dados_checkout = response.json()

        # pegando a url de pagamento
        url_pagamento = None
        for link in dados_checkout['links']:
            if link['rel'] == 'PAY':
                url_pagamento = link['href']
                break

        if url_pagamento:
            # Redireciona o usuário para a URL de pagamento
            return redirect(url_pagamento)
        else:
            # Se a URL de pagamento não for encontrada, retorna uma resposta de erro
            return HttpResponse('URL de pagamento não encontrada', status=500)

    else:
        # Se a requisição falhar, retorna uma resposta de erro
        return HttpResponse('Erro ao criar o checkout', status=response.status_code)
