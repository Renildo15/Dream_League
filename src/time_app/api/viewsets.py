from rest_framework import viewsets
from time_app.api import serializers
from time_app.models import Time, Idolo

class IdoloViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IdoloSerializers
    queryset = Idolo.objects.all()

class TimeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TimeSerializers
    queryset = Time.objects.all()