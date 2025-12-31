from .views import  WeatherAPIView
from django.urls import path

urlpatterns= [
    path('weather/', WeatherAPIView.as_view())

]
