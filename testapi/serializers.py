from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Car


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password =self.validated_data['password'],
            email=self.validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    class Meta:
        model = User
        fields = ('username', 'password', 'email',)


class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ('id','reg_num', 'max_passenger', 'manufacture_year', 'manufacturer', 'car_model','car_category','car_motor')
    

