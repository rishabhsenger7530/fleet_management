from django.db import models

from car.choices import CAR_MOTOR_CHOICES, CATEGORY_CHOICES


class CarManufacurer(models.Model):
    manufacturer = models.CharField(max_length=250)

    def __str__(self):
        return self.manufacturer

class CarModel(models.Model):
     manufacturer = models.ForeignKey(CarManufacurer, related_name='carmodel', on_delete=models.CASCADE)
     model_type = models.CharField(max_length=250)

     def __str__(self):
         return self.model_type

class Car(models.Model):
    registration_no = models.CharField(max_length=50, unique=True)
    max_passenger = models.PositiveIntegerField(default=1)
    manufacture_year = models.PositiveIntegerField(default=2021)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='car')
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES)
    motor = models.CharField(max_length=15, choices=CAR_MOTOR_CHOICES)

    def __str__(self):
        return self.registration_no+' '+self.category
