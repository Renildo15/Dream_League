from django.db import models
#from time_app.models import Time
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Competicao(models.Model):
    id_competicao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_competicao = models.CharField(max_length=200)
    temporada = models.PositiveIntegerField(null=True,blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    emblema = models.ImageField(null=True, blank=True)
    campeoes = models.ManyToManyField('time_app.Time', blank=True)


    def __str__(self):
        return self.nome_competicao