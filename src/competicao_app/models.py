from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.


class Campeonato(models.Model):

    choice_tipo = (
        ('Liga', 'Liga'),
        ('Copa', 'Copa'),
        ('Copa Internacional', 'Copa Internacional')
    )
    id_competicao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_competicao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200, choices=choice_tipo, null=True, blank=True)
    num_times = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    emblema = models.ImageField(null=True, blank=True)
    temporada = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    regras = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome_competicao


class Campeao(models.Model):
    id_campeao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    campeao = models.ForeignKey('time_app.Time', on_delete=models.SET_NULL, null=True, blank=True)
    num_titulos = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    campeonato = models.ForeignKey(Campeonato, on_delete=models.SET_NULL, blank=True, null=True, related_name='campeao')

    class Meta:
        ordering = ('num_titulos',)
    
    def __str__(self):
        return f"{self.campeao.nome_time} - {self.num_titulos}"
