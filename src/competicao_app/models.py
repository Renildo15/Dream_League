from django.db import models
#from time_app.models import Time
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Titulo(models.Model):
    id_competicao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_competicao = models.CharField(max_length=200)
    num_times = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    num_titulos = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    emblema = models.ImageField(null=True, blank=True)
    temporada = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    regras = models.CharField(max_length=200)
    campeoes = models.ForeignKey('time_app.Time', blank=True, null=True,on_delete=models.CASCADE, related_name='titulo')


    def __str__(self):
        return self.nome_competicao

  