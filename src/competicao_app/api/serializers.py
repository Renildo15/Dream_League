from rest_framework import serializers
from competicao_app.models import Titulo

class CompeticaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = ['id_competicao', 'nome_competicao','num_times', 'num_titulos', 'emblema', 'temporada', 'regras', 'campeoes']
        label = {
            'campeoes': 'campeao'
        }