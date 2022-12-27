# Generated by Django 4.1.4 on 2022-12-27 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores_app', '0004_remove_jogador_time_jogador'),
        ('time_app', '0012_remove_time_jogadores_time_jogadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='jogadores',
        ),
        migrations.AddField(
            model_name='time',
            name='jogadores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jogadores_app.jogador'),
        ),
    ]