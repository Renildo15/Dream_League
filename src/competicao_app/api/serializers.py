from rest_framework import serializers
from competicao_app.models import Campeonato, Campeao


class CampeaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Campeao
        fields = ['id_campeao','time_campeao','num_titulos', 'campeonato']


class CompeticaoSerializers(serializers.ModelSerializer):
    campeao = CampeaoSerializers(many=True, read_only=True)
    campeao= serializers.StringRelatedField(many=True)
    class Meta:
        model = Campeonato
        fields = ['id_competicao', 'nome_competicao', 'tipo','num_times', 'emblema', 'temporada', 'regras','campeao']
        
        