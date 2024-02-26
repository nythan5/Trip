from django import forms
from trip import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['titulo', 'is_active']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
