# Generated by Django 5.0.2 on 2024-03-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0007_alter_viagem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='custo',
            field=models.FloatField(),
        ),
    ]