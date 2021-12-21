from datetime import date

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _




# Create your models here.

def current_year():
    return date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    


CATEGORY_CHOICES = (
    ("Economy", "Economy"),
    ("Business", "Business"),
    ("First_Class", "First_Class)"),
 
)

CAR_MOTOR_CHOICES = (
    ("Hybrid", "Hybrid"),
    ("Electric_Motor", "Electric_Motor"),
)

class User(AbstractUser):
    contact = models.CharField(max_length=250, null =False, blank=False)
    email = models.EmailField(max_length=250)
    

  
class Car(models.Model):
    reg_num = models.CharField(max_length=50,unique=True, blank=False,null=False)
    max_passenger = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(100),MinValueValidator(1)])
    manufacture_year = models.IntegerField(_('year'), validators=[MinValueValidator(1984), max_value_current_year])
    manufacturer = models.CharField(max_length=250, blank=False,null=False)
    car_model =  models.CharField(max_length=250, blank=False,null=False)
    car_category = models.CharField(max_length = 12, choices = CATEGORY_CHOICES)
    car_motor = models.CharField(max_length = 15, choices = CAR_MOTOR_CHOICES)

 