# Generated by Django 4.1.4 on 2023-01-03 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0023_alter_time_ano_fundacao'),
        ('competicao_app', '0008_alter_campeao_campeonato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeao',
            name='campeao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='time_app.time'),
        ),
    ]
