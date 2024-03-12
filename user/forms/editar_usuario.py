from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class EditUserForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email')

    # Widgets para personalizar a aparência dos campos
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        'password_confirm': forms.PasswordInput(attrs={'class': 'form-control'}),
    }

    # Labels personalizados
    labels = {
        'username': 'Nome de Usuário',
        'email': 'Endereço de Email',
        'password': 'Nova Senha',
        'password_confirm': 'Confirmação de Senha',
    }

    # Texto de ajuda personalizado
    help_texts = {
        'password': 'Use uma senha forte e segura.',
        'password_confirm': 'Repita a nova senha para confirmação.',
    }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('As senhas não coincidem.')

        return password_confirm
