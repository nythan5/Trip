from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Viagem, Categoria
from .forms.categoria_form import CategoriaForm
from .forms.viagem_form import ViagemForm
from django.contrib import messages


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


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        categoria.delete()
        messages.success(request, 'Categoria deletada com sucesso.')
        return redirect('trip:listar_categorias')

    return render(request, 'trip/categoria/excluir_categoria.html',
                  {'categoria': categoria})


def atualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid:
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso.')
            return redirect('trip:listar_categorias')

    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'trip/categoria/atualizar_categoria.html',
                  {'form': form, 'categoria': categoria})


def criar_viagem(request):
    if request.method == "POST":
        post_data = request.POST.copy()
        post_data['custo'] = post_data['custo'].replace(',', '.')
        post_data['preco'] = post_data['preco'].replace(',', '.')

        form = ViagemForm(post_data)
        if form.is_valid():
            form.save()
            return redirect('trip:listar_viagens')
    else:
        form = ViagemForm()
    return render(request, 'trip/viagem/criar_viagem.html', {'form': form})


def listar_viagens(request):
    viagens = Viagem.objects.all().order_by('-id')
    return render(request, 'trip/viagem/listar_viagens.html',
                  {'viagens': viagens})


def atualizar_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)

    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['custo'] = request.POST['custo'].replace(',', '.')
        request.POST['preco'] = request.POST['preco'].replace(',', '.')
        form = ViagemForm(request.POST, instance=viagem)
        if form.is_valid:
            form.save()
            return redirect('trip:listar_viagens')

    else:
        form = ViagemForm(instance=viagem)

    return render(request, 'trip/viagem/atualizar_viagem.html',
                  {'form': form, 'viagem': viagem})


def excluir_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)

    if request.method == "POST":
        viagem.delete()
        return redirect('trip:listar_viagens')

    return render(request, 'trip/viagem/excluir_viagem.html',
                  {'viagem': viagem})
