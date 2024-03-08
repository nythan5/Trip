from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Categoria(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


@receiver(post_save, sender=Categoria)
def atualizar_viagens_com_categoria(sender, instance, **kwargs):
    if not instance.is_active:
        # Se a categoria foi desativada, atualizar todas as viagens associadas para None
        Viagem.objects.filter(categoria=instance).update(categoria=None)


class Viagem(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, default=None)  # noqa
    descricao = models.TextField(null=False)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    check_in_data = models.DateTimeField(null=False)
    check_out_data = models.DateTimeField(null=False)
    vagas_disponiveis = models.IntegerField()
    # cover = models.ImageField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.titulo)

    def save(self, *args, **kwargs):
        if self.titulo and (not self.slug or slugify(self.titulo) != self.slug):  # noqa
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
