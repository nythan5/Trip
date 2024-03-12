from django.contrib import admin
from .models import Cliente

# Register your models here.


@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at',]
    list_display_links = ['id', 'user']
    search_fields = ['id', 'user',]
    list_per_page = 10
    ordering = '-id',
