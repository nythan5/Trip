from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Viagem, Categoria
from .forms.categoria_form import CategoriaForm
from .forms.viagem_form import ViagemForm
from django.contrib import messages
from user.models import ViagensCliente


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
    return render(request, 'trip/categoria/listar_categorias.html',
                  {'categorias': categorias})


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
                  {'form': form, 'categoria': categoria})


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        categoria.delete()
        messages.success(request, 'Categoria deletada com sucesso.')
        return redirect('trip:listar_categorias')

    return render(request, 'trip/categoria/listar_categorias.html',
                  {'categoria': categoria})


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
    return render(request, 'trip/viagem/criar_viagem.html', {'form': form, })


def listar_viagens(request):
    viagens = Viagem.objects.all().order_by('-id')
    categorias = Categoria.objects.filter(is_active=True).order_by('-id')
    return render(request, 'trip/viagem/listar_viagens.html',
                  {'viagens': viagens, 'categorias': categorias})


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
                  {'form': form, 'viagem': viagem, })


def excluir_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)

    if request.method == "POST":
        viagem.delete()
        messages.success(request, "Viagem deletada com sucesso!")
        return redirect('trip:listar_viagens')

    return render(request, 'trip/viagem/listar_viagens.html',
                  {'viagem': viagem})


def listar_viagens_disponiveis(request):
    # Filtra as viagens que estão ativas e têm vagas disponíveis
    viagens_disponiveis = Viagem.objects.filter(
        is_active=True, vagas_disponiveis__gt=0)

    return render(request, 'home.html', {'viagens_disponiveis': viagens_disponiveis})
