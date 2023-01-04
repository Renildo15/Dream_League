# Generated by Django 4.1.4 on 2023-01-04 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0023_alter_time_ano_fundacao'),
        ('competicao_app', '0013_rename_campeonato_campeonato_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campeao',
            name='campeao',
        ),
        migrations.RemoveField(
            model_name='campeonato',
            name='time',
        ),
        migrations.AddField(
            model_name='campeao',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campeao', to='time_app.time'),
        ),
    ]
