from django.urls import path
from testapi import views


urlpatterns = [
    path('create', views.CreateCarView.as_view()),
    path('list', views.ListCarView.as_view()),
    path('retrieve/<int:pk>', views.RetrieveCarView.as_view()),
    path('update/<int:pk>', views.UpdateCarView.as_view()),
]


