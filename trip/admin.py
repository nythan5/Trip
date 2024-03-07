from django.contrib import admin
from .models import Categoria, Viagem

# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'created_at', 'updated_at', 'is_active',]
    list_display_links = ['id', 'titulo']
    search_fields = ['id', 'titulo',]
    list_per_page = 10
    ordering = '-id',


@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'created_at', 'updated_at', 'is_active',]
    list_display_links = ['id', 'titulo']
    search_fields = ['id', 'titulo',]
    list_per_page = 10
    ordering = '-id',
