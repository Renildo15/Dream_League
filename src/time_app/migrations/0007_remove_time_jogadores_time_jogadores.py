# Generated by Django 4.1.4 on 2022-12-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0006_time_jogadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='jogadores',
        ),
        migrations.AddField(
            model_name='time',
            name='jogadores',
            field=models.IntegerField(default=0),
        ),
    ]
