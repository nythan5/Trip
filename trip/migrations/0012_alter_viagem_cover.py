# Generated by Django 5.0.2 on 2024-03-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0011_alter_viagem_vagas_disponiveis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='cover',
            field=models.ImageField(upload_to=''),
        ),
    ]
