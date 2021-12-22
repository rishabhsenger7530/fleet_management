from django.contrib import admin

from car.models import Car, CarManufacurer, CarModel


@admin.register(CarManufacurer)
class CarManufacurerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer']

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['registration_no','max_passenger', 'manufacture_year', 'model', 'category', 'motor']
