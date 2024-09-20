from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import CalculadoraInversionResponseSerializer, CalculadoraInversionRequestSerializer
from .classes import MyResponse, Producto
from django.utils.dateparse import parse_date

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Producto
from .serializers import ProductoSerializer

class ProductoListView(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CustomObjectView(APIView):
    def get(self, request):
        serializer = CalculadoraInversionRequestSerializer(data = request.query_params)
        serializer.is_valid(raise_exception=True)
        requestData = serializer.validated_data
        
        producto = requestData['producto']
        enReinversion = requestData['enReinversion']
        plazo = requestData['plazo']
        fecha_creacion = requestData['fechaCreacion']
        
        producto1 = Producto(1,2,1,3,2)
        
        custom_data = MyResponse(
            1, 
            33, 
            "2022-07-14 00:00:00", 
            "2022-08-17 00:00:00", 
            34)

        # Serialize the data
        response_serializer = CalculadoraInversionResponseSerializer(custom_data)

        # Return the serialized data as a response
        return Response(response_serializer.data)
