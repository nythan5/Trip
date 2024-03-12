from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Widgets para personalizar a aparência dos campos
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
    }

    # Labels personalizados
    labels = {
        'username': 'Nome de Usuário',
        'email': 'Endereço de Email',
        'password1': 'Senha',
        'password2': 'Confirmação de Senha',
    }

    # Texto de ajuda personalizado
    help_texts = {
        'password1': 'Use uma senha forte e segura.',
        'password2': 'Repita a senha para confirmação.',
    }
