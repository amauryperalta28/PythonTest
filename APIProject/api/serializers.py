from rest_framework import serializers
from .classes import MyResponse


class MyRequestSerializer(serializers.Serializer):
    producto = serializers.CharField()
    enReinversion = serializers.BooleanField()
    plazo = serializers.IntegerField()
    fechaCreacion = serializers.CharField()


class MyResponseSerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    plazo = serializers.IntegerField()
    fechaInicio = serializers.DateField()
    fechaFin = serializers.DateField()
    plazoReal = serializers.IntegerField()
