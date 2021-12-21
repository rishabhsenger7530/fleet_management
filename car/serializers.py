from rest_framework import serializers

from car.models import Car

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ('id','registration_no', 'max_passenger', 'manufacture_year', 'manufacturer', 'model','category','motor')
    