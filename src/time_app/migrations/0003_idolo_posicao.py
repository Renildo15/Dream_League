# Generated by Django 4.1.4 on 2022-12-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_app', '0002_rename_id_time_idolo_id_idolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='idolo',
            name='posicao',
            field=models.CharField(blank=True, choices=[('GK', 'GK'), ('ZE', 'ZE'), ('ZD', 'ZD'), ('LE', 'LE'), ('LD', 'LD'), ('V', 'V'), ('ME', 'ME'), ('MD', 'MD'), ('MAT', 'MAT'), ('MLG', 'MLG'), ('PTD', 'PTD'), ('PTE', 'PTE'), ('SA', 'SA'), ('ATA', 'ATA')], max_length=200, null=True),
        ),
    ]
