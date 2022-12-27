# Generated by Django 4.1.4 on 2022-12-27 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores_app', '0005_jogador_time'),
        ('time_app', '0014_remove_time_jogadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='jogadores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jogadores_time', to='jogadores_app.jogador'),
        ),
    ]
