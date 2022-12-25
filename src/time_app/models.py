from django.db import models
from uuid import uuid4

# Create your models here.

class Idolo(models.Model):
    id_time = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200)

class Time(models.Model):
    id_time = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_time = models.CharField(max_length=200)
    num_jogadores = models.IntegerField(default=0)
    titulos = models.IntegerField(default=0)
    total_titulos = models.IntegerField(default=0)
    idolo = models.ForeignKey(Idolo, on_delete=models.CASCADE, blank=True, null=True)
    escudo = models.ImageField(null=True, blank=True)
    nome_estadio = models.CharField(max_length=200)
    ano_fundacao = models.IntegerField(default=0)


