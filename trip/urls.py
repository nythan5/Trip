# flake8: noqa
from django.urls import path
from .views import *

app_name = 'trip'

urlpatterns = [
    path('', listar_viagens_disponiveis,
         name='home'),
    path('criar_categoria/', criar_categoria, name='criar_categoria'),
    path('listar_categorias/', listar_categorias, name='listar_categorias'),
    path('excluir_categoria/<int:categoria_id>',
         excluir_categoria, name='excluir_categoria'),
    path('atualizar_categoria/<int:categoria_id>',
         atualizar_categoria, name='atualizar_categoria'),
    path('criar_viagem/', criar_viagem, name='criar_viagem'),
    path('listar_viagens/', listar_viagens, name='listar_viagens'),
    path('atualizar_viagem/<int:viagem_id>',
         atualizar_viagem, name='atualizar_viagem'),
    path('excluir_viagem/<int:viagem_id>',
         excluir_viagem, name='excluir_viagem'),

]
