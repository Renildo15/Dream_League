# Generated by Django 4.1.4 on 2022-12-25 12:44

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idolo',
            fields=[
                ('id_time', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('nacionalidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id_time', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_time', models.CharField(max_length=200)),
                ('num_jogadores', models.IntegerField(default=0)),
                ('titulos', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('total_titulos', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('escudo', models.ImageField(blank=True, null=True, upload_to='')),
                ('nome_estadio', models.CharField(max_length=200)),
                ('ano_fundacao', models.PositiveIntegerField(help_text='Use the following format: <YYYY>', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)])),
                ('idolo', models.ManyToManyField(blank=True, to='time_app.idolo')),
            ],
        ),
    ]
