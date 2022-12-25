from rest_framework import serializers
from jogadores_app.models import Jogador

class JogadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'