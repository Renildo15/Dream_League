# Generated by Django 4.1.4 on 2022-12-31 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competicao_app', '0004_titulo_delete_competicao'),
    ]

    operations = [
        migrations.AddField(
            model_name='titulo',
            name='num_times',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
