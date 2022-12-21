from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('weather_1', views.get_weather),
    path('index', views.index)

]