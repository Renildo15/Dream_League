from rest_framework import serializers
from competicao_app.models import Competicao
from time_app.api.serializers import TimeSerializers

class CompeticaoSerializers(serializers.ModelSerializer):
    campeoes = TimeSerializers(many=True, read_only=True)
    class Meta:
        model = Competicao
        fields = ['id_competicao', 'nome_competicao', 'num_titulos', 'emblema', 'temporada', 'regras', 'campeoes']