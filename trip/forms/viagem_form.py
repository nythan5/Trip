from django import forms
from trip import models
from utils.placeholder_forms import add_placeholder
from django.forms.widgets import NumberInput


class ViagemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ViagemForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = models.Categoria.objects.filter(
            is_active=True).order_by('-id')

        add_placeholder(self.fields['titulo'],
                        'Digite um titulo para a viagem')
        add_placeholder(self.fields['descricao'],
                        'Digite uma descricao para a viagem')
        add_placeholder(self.fields['check_in_data'],
                        'Selecione a data de Check-In')
        add_placeholder(self.fields['check_out_data'],
                        'Selecione a data de Check-Out')
        add_placeholder(self.fields['custo'],
                        '00.00')
        add_placeholder(self.fields['preco'],
                        '00.00')

    class Meta:
        model = models.Viagem
        fields = ['titulo', 'categoria', 'descricao', 'custo',
                  'preco', 'check_in_data', 'check_out_data',
                  'vagas_disponiveis', 'is_active']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'check_in_data': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'check_out_data': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'custo': forms.TextInput(attrs={'class': 'form-control money-mask'}),
            'preco': forms.TextInput(attrs={'class': 'form-control money-mask'}),
            'vagas_disponiveis': forms.TextInput(attrs={'class': 'form-control'}),


        }

        labels = {
            'is_active': 'Status',
            'check_in_data': 'Data de Check-In',
            'check_out_data': 'Data de Check-Out',

        }
