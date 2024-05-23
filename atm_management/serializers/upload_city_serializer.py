from rest_framework import serializers


class CityDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    
