# Generated by Django 5.0.2 on 2024-03-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0014_alter_viagem_custo_alter_viagem_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='cover',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]