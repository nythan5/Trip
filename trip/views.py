from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Categoria
from .forms.categoria_form import CategoriaForm


def criar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'trip/criar_categoria.html', {'form': form})


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'trip/listar_categorias.html',
                  {'categorias': categorias})


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        categoria.delete()
        return redirect('trip:listar_categorias')

    return render(request, 'trip/excluir_categoria.html',
                  {'categoria': categoria})


def atualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid:
            form.save()
            return redirect('trip:listar_categorias')

    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'trip/atualizar_categoria.html', {'form': form, 'categoria': categoria})
