from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name',
            'last_name', 'password1', 'password2'
        ]

        # Widgets para personalizar a aparência dos campos
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
        }

        # Labels personalizados
        labels = {
            'username': 'Nome de Usuário',
            'email': 'Endereço de Email',
            'first_name': 'Primeiro Nome',
            'last_name': 'Último Nome',
            'password1': 'Senha',
            'password2': 'Confirmação de Senha',
        }
