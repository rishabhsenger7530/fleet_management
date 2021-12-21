from car.models import Car
from car.serializers import CarSerializer
from car.utils import get_object

from rest_framework import generics


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
