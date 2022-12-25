from rest_framework import serializers
from time_app.models import Time, Idolo

class IdoloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Idolo
        fields = '__all__'

    

class TimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'