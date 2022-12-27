# Generated by Django 4.1.4 on 2022-12-27 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0019_remove_time_jogadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='idolo',
        ),
        migrations.RemoveField(
            model_name='time',
            name='titulos',
        ),
        migrations.AddField(
            model_name='idolo',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='time_app.time'),
        ),
    ]