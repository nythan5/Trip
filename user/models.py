from django.contrib.auth.models import User
from django.db import models
from trip.models import Viagem


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(null=False)
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    )
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ViagensCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.user.username} - {self.viagem.titulo}"
