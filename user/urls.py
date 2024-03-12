from django.urls import path
from .views import criar_usuario, listar_usuarios, excluir_usuario, editar_usuario

app_name = 'user'

urlpatterns = [

    path('criar_usuario/', criar_usuario, name='criar_usuario'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('excluir_usuario/<int:user_id>/',
         excluir_usuario, name='excluir_usuario'),
    path('editar_usuario/<int:user_id>/',
         editar_usuario, name='editar_usuario'),

]
