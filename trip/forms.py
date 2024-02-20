from django import forms
from .models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['titulo', 'is_active']
        labels = {'is_active': 'Ativo'}
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Insira o título da categoria'})
        }
