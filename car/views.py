from rest_framework import generics, viewsets

from car.models import Car, CarManufacurer, CarModel
from car.serializers import (CarManufacurerSerializer, CarModelSerializers,
                             CarSerializer)
from car.utils import get_object


class CreateCarView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    format = None

class ListCarView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return get_object(self)
       
class RetrieveCarView(generics.RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class UpdateCarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarManufacturerViewSet(viewsets.ModelViewSet):
    queryset = CarManufacurer.objects.all()
    serializer_class = CarManufacurerSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializers