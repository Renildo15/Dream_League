from rest_framework import serializers
from competicao_app.models import Competicao

class CompeticaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Competicao
        fields = '__all__'