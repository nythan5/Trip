from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active')
        # Widgets para personalizar a aparência dos campos
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        # Labels personalizados
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Último Nome',
            'email': 'Endereço de Email',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remova o campo de senha do formulário
        del self.fields['password']
