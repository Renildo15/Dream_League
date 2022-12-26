from rest_framework import serializers
from time_app.models import Time, Idolo
from jogadores_app.api.serializers import JogadorSerializers

class IdoloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Idolo
        fields = '__all__'

    

class TimeSerializers(serializers.ModelSerializer):
    #idolo = IdoloSerializers(many=True, read_only=True)
    #jogadores = JogadorSerializers(many=True, read_only=True)
    class Meta:
        model = Time
        fields = ['id_time', 'nome_time','jogadores','num_jogadores','titulos','total_titulos','idolo','escudo', 'federacao', 'nome_estadio', 'ano_fundacao']