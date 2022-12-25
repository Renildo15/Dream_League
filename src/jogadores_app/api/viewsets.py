from rest_framework import viewsets
from jogadores_app.api.serializers import JogadorSerializers
from jogadores_app.models import Jogador

class JogadoresViewSet(viewsets.ModelViewSet):
    serializer_class = JogadorSerializers
    queryset = Jogador.objects.all()