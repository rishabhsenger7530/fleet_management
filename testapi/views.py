from rest_framework import generics
from django.shortcuts import render

from .models import User, Car
from .serializers import UserSerializer, CarSerializer

# Create your views here.



class CreateCarView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    format = None


class ListCarView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    


class RetrieveCarView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class UpdateCarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

