from rest_framework import serializers
from time_app.models import Time, Idolo
from jogadores_app.api.serializers import JogadorSerializers
from competicao_app.api.serializers import CompeticaoSerializers, CampeaoSerializers

class IdoloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Idolo
        fields = ['id_idolo','nome', 'posicao', 'nacionalidade', 'time']

    

class TimeSerializers(serializers.ModelSerializer):
    idolo = IdoloSerializers(many=True, read_only=True)
    jogadores = JogadorSerializers(many=True, read_only=True)
    campeao = CampeaoSerializers(many=True, read_only=True)
    campeao= serializers.StringRelatedField(many=True)
    class Meta:
        model = Time
        fields = ['id_time', 'nome_time','jogadores','num_jogadores','total_titulos','escudo', 'federacao', 'nome_estadio', 'ano_fundacao', 'idolo', 'campeao']



