from django import forms
from user.models import Cliente
from utils.placeholder_forms import add_placeholder


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['rg'], 'Digite o RG')
        add_placeholder(self.fields['cpf'], 'Digite o CPF')
        add_placeholder(self.fields['telefone'], 'Digite o telefone')

    class Meta:
        model = Cliente
        fields = ['rg', 'cpf', 'telefone', 'data_nascimento', 'genero']

        widgets = {
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'data_nascimento': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }
