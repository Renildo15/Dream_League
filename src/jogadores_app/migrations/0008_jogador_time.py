# Generated by Django 4.1.4 on 2022-12-27 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0019_remove_time_jogadores'),
        ('jogadores_app', '0007_remove_jogador_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='time_app.time'),
        ),
    ]
