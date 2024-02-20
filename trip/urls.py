from django.urls import path
from .views import *

app_name = 'trip'

urlpatterns = [
    path('criar_categoria/', criar_categoria_view, name='criar_categoria'),
    path('listar_categorias/', listar_categorias_view, name='listar_categorias')

]
