from django.shortcuts import render, redirect, get_object_or_404
from .forms.criar_usuario_form import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms.editar_usuario import EditUserForm

# Create your views here.


def criar_usuario(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Substitua 'página_de_sucesso' pela URL desejada
            return redirect('user:listar_usuarios')
    else:
        form = CreateUserForm()

    return render(request, 'user/criar_usuario.html', {'form': form})


def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'user/listar_usuarios.html', {'usuarios': usuarios})


def excluir_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        usuario.delete()
        messages.success(request, 'Usuário deletado com sucesso.')
        return redirect('user:listar_usuarios')

    return render(request, "user/excluir_usuario.html", context={'usuario': usuario})  # noqa


def editar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario atualizado com sucesso.')
            # Substitua pelo nome da sua página de perfil
            return redirect('user:listar_usuarios')
    else:
        form = EditUserForm(instance=usuario)

    return render(request, 'user/editar_usuario.html', {'form': form, 'usuario': usuario})  # noqa
