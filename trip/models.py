from django.db import models

# Create your models here.


class Categoria(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
