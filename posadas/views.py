from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from posadas.models import Posada
from posadas.serializers import PosadaSerializer

# Create your views here.


class ListGenericPosada(generics.ListCreateAPIView):
    queryset = Posada.objects.all()
    serializer_class = PosadaSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class DetailGenericPosada(generics.RetrieveUpdateAPIView):
    queryset = Posada.objects.all()
    serializer_class = PosadaSerializer
