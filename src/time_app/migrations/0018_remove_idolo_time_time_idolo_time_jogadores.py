# Generated by Django 4.1.4 on 2022-12-27 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores_app', '0007_remove_jogador_time'),
        ('time_app', '0017_remove_time_idolo_idolo_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idolo',
            name='time',
        ),
        migrations.AddField(
            model_name='time',
            name='idolo',
            field=models.ManyToManyField(blank=True, to='time_app.idolo'),
        ),
        migrations.AddField(
            model_name='time',
            name='jogadores',
            field=models.ManyToManyField(blank=True, to='jogadores_app.jogador'),
        ),
    ]