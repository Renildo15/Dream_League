# Generated by Django 4.1.4 on 2022-12-27 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0014_remove_time_jogadores'),
        ('jogadores_app', '0004_remove_jogador_time_jogador'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='time_app.time'),
        ),
    ]
