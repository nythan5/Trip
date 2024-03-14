from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [

    path('criar_usuario/', criar_usuario, name='criar_usuario'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('excluir_usuario/<int:user_id>/',
         excluir_usuario, name='excluir_usuario'),
    path('editar_usuario/<int:user_id>/',
         editar_usuario, name='editar_usuario'),

    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('vincular_viagem/<int:viagem_id>',
         vincular_viagem, name='vincular_viagem'),
    path('excluir_viagem_vinculada/<int:viagem_cliente_id>/',
         excluir_viagem_vinculada, name='excluir_viagem_vinculada'),

]
