from django.shortcuts import render, redirect
from django.views import View
from .models import Categoria
from .forms import CategoriaForm


def criar_categoria_view(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin')
    else:
        form = CategoriaForm()
    return render(request, 'trip/criar_categoria.html', {'form': form})


def listar_categorias_view(request):
    categorias = Categoria.objects.all()
    return render(request, 'trip/listar_categorias.html',
                  {'categorias': categorias})
