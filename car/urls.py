from django.urls import include, path
from rest_framework import routers

from car import views

router = routers.DefaultRouter()
router.register(r"carmodel", views.CarModelViewSet)
router.register(r"car_manufacturer", views.CarManufacturerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('car:create', views.CreateCarView.as_view()),
    path('car:list', views.ListCarView.as_view()),
    path('car:retrieve/<int:pk>', views.RetrieveCarView.as_view()),
    path('car:update/<int:pk>', views.UpdateCarView.as_view()),
]
