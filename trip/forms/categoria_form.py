from django import forms
from trip import models
from utils.placeholder_forms import add_placeholder


class CategoriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['titulo'],
                        'Digite um titulo para a categoria')

    class Meta:
        model = models.Categoria
        fields = ['titulo', 'is_active',]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'is_active': 'Status',
        }
