from rest_framework import viewsets
from competicao_app.api import serializers
from competicao_app.models import Titulo

class CompeticaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompeticaoSerializers
    queryset = Titulo.objects.all()