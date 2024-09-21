from rest_framework import serializers
from .models import Producto

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class CalculadoraInversionRequestSerializer(serializers.Serializer):
    producto = serializers.CharField()
    enReinversion = serializers.BooleanField()
    plazo = serializers.IntegerField()
    fechaCreacion = serializers.CharField()


class CalculadoraInversionResponseSerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    plazo = serializers.IntegerField()
    fechaInicio = serializers.DateField()
    fechaFin = serializers.DateField()
    plazoReal = serializers.IntegerField()


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'dias_fecha_previa_igual', 
                  'dias_fecha_previa_igual_con_reinversion', 
                  'dias_horario_posterior_igual', 
                  'dias_horario_posterior_igual_con_reinversion']

