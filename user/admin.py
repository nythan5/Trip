from django.contrib import admin
from .models import Cliente

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
