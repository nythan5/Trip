# Generated by Django 5.0.2 on 2024-03-07 12:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_categoria_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
