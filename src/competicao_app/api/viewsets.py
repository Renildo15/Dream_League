from rest_framework import viewsets
from competicao_app.api import serializers
from competicao_app.models import Campeonato, Campeao

class CompeticaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompeticaoSerializers
    queryset = Campeonato.objects.all()


class CampeaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CampeaoSerializers
    queryset = Campeao.objects.all().order_by('-num_titulos')