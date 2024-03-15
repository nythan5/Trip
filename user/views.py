from .models import Viagem
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms.criar_usuario_form import CreateUserForm
from .forms.cliente_form import ClienteForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms.editar_usuario import EditUserForm
from django.contrib import messages
from django.db import IntegrityError
from .models import ViagensCliente
from trip.models import Viagem
# Create your views here.


def criar_usuario(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # Substitua 'página_de_sucesso' pela URL desejada
                return redirect('user:listar_usuarios')
            except IntegrityError:
                messages.error(
                    request, 'Já existe um usuário com este username.')
    else:
        form = CreateUserForm()

    return render(request, 'user/criar_usuario.html', {'form': form})


def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'user/listar_usuarios.html', {'usuarios': usuarios})


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

    return render(request, 'user/listar_usuarios.html', {'form': form, 'usuario': usuario})  # noqa


def excluir_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        usuario.delete()
        messages.success(request, 'Usuário deletado com sucesso.')
        return redirect('user:listar_usuarios')

    return render(request, "user/listar_usuarios.html", context={'usuario': usuario})  # noqa


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                cliente = form.save(commit=False)
                # Associe o usuário atual ao cliente
                cliente.user = request.user
                cliente.save()
                # alterar para home do cliente
                return redirect('user:listar_usuarios')
            except IntegrityError:
                messages.error(
                    request, 'Já existe um cliente associado a este usuário.')
    else:
        form = ClienteForm()

    return render(request, 'cliente/cadastrar_cliente.html', {'form': form})


def vincular_viagem(request, viagem_id):

    if not request.user.is_authenticated:
        messages.info(request, 'Você precisa estar logado para se cadastrar.')
        return redirect('trip:home')

    # Assume-se que cada usuário tem um perfil de cliente associado
    cliente = request.user.cliente

    try:
        viagem = Viagem.objects.get(id=viagem_id)

        # Verifica se o cliente já está vinculado a esta viagem
        if ViagensCliente.objects.filter(cliente=cliente, viagem=viagem).exists():
            messages.warning(request, 'Você já está cadastrado nesta viagem.')
        else:
            # Cria uma nova entrada na tabela de associação
            ViagensCliente.objects.create(cliente=cliente, viagem=viagem)
            messages.success(
                request, 'Cadastro na viagem realizado com sucesso.')

    except Viagem.DoesNotExist:
        messages.error(request, 'Viagem não encontrada.')

    return redirect('trip:home')


def excluir_viagem_vinculada(request, viagem_cliente_id):
    if request.method == 'POST':
        # Obtém a viagem cliente a ser excluída
        viagem_cliente = get_object_or_404(
            ViagensCliente, id=viagem_cliente_id)
        # Exclui a viagem cliente
        viagem_cliente.delete()
        # Redireciona para alguma página após a exclusão
        return redirect('trip:listar_viagens_vinculadas')
    else:
        # Se o método da requisição não for POST, redireciona para a página inicial
        return redirect('trip:listar_viagens_vinculadas')
