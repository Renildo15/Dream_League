# Generated by Django 4.1.4 on 2022-12-27 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0015_time_jogadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='jogadores',
        ),
    ]
