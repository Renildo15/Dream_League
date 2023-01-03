# Generated by Django 4.1.4 on 2023-01-03 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competicao_app', '0009_alter_campeao_campeao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campeao',
            name='campeonato',
        ),
        migrations.AddField(
            model_name='campeao',
            name='campeonato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campeao', to='competicao_app.campeonato'),
        ),
    ]
