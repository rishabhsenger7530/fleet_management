from rest_framework import serializers

from car.models import Car, CarManufacurer, CarModel


class CarManufacurerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarManufacurer
        fields = ['id', 'manufacturer']

class CarModelSerializers(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='carmanufacurer-detail', lookup_field='pk')

    class Meta:
        model = CarModel
        fields = '__all__'
      
class CarSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='carmodel-detail', lookup_field='pk')
 
    class Meta:
        model = Car
        fields = '__all__'
   