from django.urls import path
from car import views

urlpatterns = [
    path('car:create', views.CreateCarView.as_view()),
    path('car:list', views.ListCarView.as_view()),
    path('car:retrieve/<int:pk>', views.RetrieveCarView.as_view()),
    path('car:update/<int:pk>', views.UpdateCarView.as_view()),
]
