# Generated by Django 5.0.2 on 2024-03-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0016_alter_viagem_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='viagens_covers/'),
        ),
    ]
