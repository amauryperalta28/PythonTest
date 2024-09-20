from rest_framework import serializers


class CalculadoraInversionRequestSerializer(serializers.Serializer):
    producto = serializers.CharField()
    enReinversion = serializers.BooleanField()
    plazo = serializers.IntegerField()
    fechaCreacion = serializers.DateField()


class CalculadoraInversionResponseSerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    plazo = serializers.IntegerField()
    fechaInicio = serializers.DateField()
    fechaFin = serializers.DateField()
    plazoReal = serializers.IntegerField()
