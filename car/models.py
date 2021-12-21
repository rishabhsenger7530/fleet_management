from django.db import models
from car.choices import CAR_MOTOR_CHOICES, CATEGORY_CHOICES


class Car(models.Model):
    registration_no = models.CharField(max_length=50, unique=True)
    max_passenger = models.PositiveIntegerField(default=1)
    manufacture_year = models.PositiveIntegerField(default=2021)
    manufacturer = models.CharField(max_length=250)
    model =  models.CharField(max_length=250)
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES)
    motor = models.CharField(max_length=15, choices= CAR_MOTOR_CHOICES)

    def __str__(self):
        return super().__str__()
