from django.urls import path
from .views import *

app_name = 'trip'

urlpatterns = [
    path('criar_categoria/', criar_categoria, name='criar_categoria'),
    path('listar_categorias/', listar_categorias, name='listar_categorias'),
    path('excluir_categoria/<int:categoria_id>',
         excluir_categoria, name='excluir_categoria'),

]
