from django.shortcuts import render, redirect
from .forms.criar_usuario_form import CreateUserForm
from django.contrib.auth.models import User

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
