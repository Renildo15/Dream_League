# Generated by Django 4.1.4 on 2022-12-25 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0007_remove_time_jogadores_time_jogadores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='jogadores',
            field=models.CharField(max_length=200),
        ),
    ]
