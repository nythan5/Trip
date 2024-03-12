from django.urls import path
from .views import criar_usuario, listar_usuarios

app_name = 'user'

urlpatterns = [

    path('criar_usuario/', criar_usuario, name='criar_usuario'),
    path('listar_usuario/', listar_usuarios, name='listar_usuarios'),

]
