from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from datetime import datetime
from uuid import uuid4

# Create your models here.

class Time(models.Model):

    fed = (
        ('FRF', 'FRF'),
        ('FMH', 'FMH'),
        ('FHV', 'FHV')
    )

    id_time = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_time = models.CharField(max_length=200)
    num_jogadores = models.IntegerField(default=0)
    total_titulos = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    escudo = models.ImageField(null=True, blank=True)
    federacao = models.CharField(max_length=200, choices=fed, null=True, blank=True)
    nome_estadio = models.CharField(max_length=200)
    ano_fundacao = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],help_text="Use the following format: <YYYY>")


    def __str__(self):

        return self.nome_time 


class Idolo(models.Model):

    pos = (
        ('GK', 'GK'),
        ('ZE', 'ZE'),
        ('ZD', 'ZD'),
        ('LE', 'LE'),
        ('LD', 'LD'),
        ('V', 'V'),
        ('ME', 'ME'),
        ('MD', 'MD'),
        ('MAT', 'MAT'),
        ('MLG', 'MLG'),
        ('PTD', 'PTD'),
        ('PTE', 'PTE'),
        ('SA', 'SA'),
        ('ATA', 'ATA'),
    )

    id_idolo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=200)
    posicao = models.CharField(max_length=200,choices=pos,blank=True, null=True)
    nacionalidade = models.CharField(max_length=200)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True, blank=True, related_name='idolo')


    def __str__(self):
        return f'{self.nome} - {self.posicao}'

