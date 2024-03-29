# flake8:noqa
from django.urls import path
from .views import *
from trip.urls import listar_viagens_vinculadas
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [

    # Usuarios
    path('criar_usuario/', criar_usuario, name='criar_usuario'),

    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),

    path('editar_usuario/<int:user_id>/',
         editar_usuario, name='editar_usuario'),

    path('excluir_usuario/<int:user_id>/',
         excluir_usuario, name='excluir_usuario'),

    # Viagens Vinculadas
    path('vincular_viagem/<int:viagem_id>',
         vincular_viagem, name='vincular_viagem'),

    path('listar_viagens_vinculadas/', listar_viagens_vinculadas,
         name='listar_viagens_vinculadas'),

    path('excluir_viagem_vinculada/<int:viagem_cliente_id>/',
         excluir_viagem_vinculada, name='excluir_viagem_vinculada'),

    # Cliente
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_clientes/', listar_clientes, name='listar_clientes'),
    path('editar_cliente/<int:cliente_id>',
         editar_cliente, name='editar_cliente'),
    path('excluir_cliente/<int:cliente_id>/',
         excluir_cliente, name='excluir_cliente'),

    # Dashboard
    path('dashboard_geral/', dashboard_geral, name='dashboard_geral'),

    # login
    path('login/', user_login, name='login'),
    path('cliente_login/', cliente_login, name='cliente_login'),

    # logout
    path('logout/', user_logout, name='logout'),
]
