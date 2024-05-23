from rest_framework import serializers


class StateDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    abbreviation = serializers.CharField(required=False,allow_blank=False, allow_null=False)
    
