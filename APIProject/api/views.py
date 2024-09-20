from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import MyResponseSerializer, MyRequestSerializer
from .classes import MyResponse
from django.utils.dateparse import parse_date
from rest_framework.exceptions import ValidationError

# Create your views here.

class CustomObjectView(APIView):
    def get(self, request):
        serializer = MyRequestSerializer(data = request.query_params)
        serializer.is_valid(raise_exception=True)
        requestData = serializer.validated_data
        
        producto = requestData['producto']
        enReinversion = requestData['enReinversion']
        plazo = requestData['plazo']
        fecha_creacion_str = requestData['fechaCreacion']
        
        fecha_creacion = parse_date(fecha_creacion_str)
        if not fecha_creacion:
            raise ValidationError("Fecha no válida. Usa el formato YYYY-MM-DD.")

        
        custom_data = MyResponse(
            1, 
            33, 
            "2022-07-14 00:00:00", 
            "2022-08-17 00:00:00", 
            34)

        # Serialize the data
        response_serializer = MyResponseSerializer(custom_data)

        # Return the serialized data as a response
        return Response(response_serializer.data)
