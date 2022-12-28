from rest_framework import serializers
from jogadores_app.models import Jogador


class JogadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ('id_jogador','nome_jogador','idade','posicao','numero','nacionalidade','status','gols','assistencias','time')
        lookup_field = 'time'