# Generated by Django 4.1.4 on 2022-12-31 12:51

from django.db import migrations, models
import time_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0021_alter_idolo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='escudo',
            field=models.ImageField(blank=True, null=True, upload_to=time_app.models.upload_image_escudo),
        ),
    ]
