from .models import Viagem
from django.shortcuts import render, redirect, get_object_or_404
from .forms.criar_usuario_form import CreateUserForm
from .forms.cliente_form import ClienteForm
from .forms.editar_cliente import ClienteEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms.editar_usuario import EditUserForm
from django.db import IntegrityError
from .models import ViagensCliente, Cliente
from trip.views import sidebar

# Create your views here.


def criar_usuario(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, 'Usuário criado com sucesso.')
                # Substitua 'página_de_sucesso' pela URL desejada
                return redirect('user:listar_usuarios')
            except IntegrityError:
                messages.error(request, 'Usuário já existe.')
                # Adicione a mensagem de erro ao formulário para que ela seja exibida no template
                form.add_error('username', 'Usuário já existe.')
    else:
        form = CreateUserForm()

    return render(request, 'user/criar_usuario.html', {'form': form, **sidebar(request)})


def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'user/listar_usuarios.html', {'usuarios': usuarios, **sidebar(request)})


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

    return render(request, 'user/listar_usuarios.html', {'form': form, 'usuario': usuario, **sidebar(request)})  # noqa


def excluir_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        usuario.delete()
        messages.success(request, 'Usuário deletado com sucesso.')
        return redirect('user:listar_usuarios')

    return render(request, "user/listar_usuarios.html", context={'usuario': usuario, **sidebar(request)})  # noqa


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
                return redirect('user:listar_clientes')
            except IntegrityError:
                messages.error(
                    request, 'Já existe um cliente associado a este usuário.')
    else:
        form = ClienteForm()

    return render(request, 'cliente/cadastrar_cliente.html', {'form': form, **sidebar(request)})


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar_clientes.html', {'clientes': clientes, **sidebar(request)})  # noqa


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        form = ClienteEditForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso.')
            # Redireciona para a lista de clientes após a edição
            return redirect('user:listar_clientes')
    else:
        print('form nao valido')
        form = ClienteEditForm(instance=cliente)

    return render(request, 'cliente/listar_clientes.html', {'form': form, **sidebar(request)})


def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == "POST":
        cliente.delete()
        messages.success(request, 'Cliente deletado com sucesso.')
        return redirect('user:listar_clientes')

    return render(request, "cliente/listar_clientes.html", {'cliente': cliente, **sidebar(request)})


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


def listar_viagens_vinculadas(request):
    if request.user.is_authenticated and request.user.groups.filter(name='ADM').exists():
        viagens_clientes = ViagensCliente.objects.filter(
            viagem__is_active=True)
        return render(request, 'trip/viagem/listar_viagens_vinculadas.html',
                      {'viagens_clientes': viagens_clientes, **sidebar(request)})

    if request.user.is_authenticated and request.user.groups.filter(name='Cliente').exists():  # noqa
        viagens_clientes = ViagensCliente.objects.filter(
            cliente=request.user.cliente)
        return render(request, 'trip/viagem/listar_viagens_vinculadas.html',
                      {'viagens_clientes': viagens_clientes, **sidebar(request)})
    else:
        messages.info(request, 'Você precisa estar logado.')
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
