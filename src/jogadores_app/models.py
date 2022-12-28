from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator 
from time_app.models import Time
# Create your models here.

class Jogador(models.Model):
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

    status_choice = (
        ('Titular', 'Titular'),
        ('Reserva', 'Reserva')
    )
    id_jogador = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_jogador = models.CharField(max_length=200)
    idade = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(99)])
    posicao = models.CharField(max_length=200, choices=pos)
    numero =  models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(99)])
    nacionalidade = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, choices=status_choice)
    gols = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(0), MaxValueValidator(2000)])
    assistencias = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(0), MaxValueValidator(2000)])
    time = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name='jogadores')
    def __str__(self):
        return self.nome_jogador