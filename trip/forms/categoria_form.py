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
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'is_active': 'Status',
        }
