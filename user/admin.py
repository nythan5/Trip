from django.contrib import admin
from .models import Cliente, ViagensCliente

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_first_name',
                    'created_at', 'rg', 'cpf', 'telefone']
    list_display_links = ['id', 'user']
    search_fields = ['id', 'user__username', 'user__first_name']
    list_per_page = 10
    ordering = '-id',

    def user_first_name(self, obj):
        return obj.user.first_name


@admin.register(ViagensCliente)
class ClienteViagensAdmin(admin.ModelAdmin):
    # Ajustado para exibir o nome de usuário do cliente e o título da viagem
    list_display = ['id', 'get_cliente_full_name', 'titulo_viagem']
    list_display_links = ['id', 'get_cliente_full_name', 'titulo_viagem']
    # Ajustado para permitir a pesquisa por nome de usuário e título da viagem
    search_fields = ['id', 'cliente__user__username', 'viagem__titulo']
    list_per_page = 10
    ordering = ['-id']

    def get_cliente_full_name(self, obj):
        # Retorna o nome completo do cliente para exibição
        return f"{obj.cliente.user.first_name} {obj.cliente.user.last_name}"

    # Define o nome da coluna na interface de administração
    get_cliente_full_name.short_description = 'Nome Completo'

    def titulo_viagem(self, obj):
        # Retorna o título da viagem vinculada ao cliente
        return obj.viagem.titulo

    # Define o nome da coluna na interface de administração
    titulo_viagem.short_description = 'Título da Viagem'
