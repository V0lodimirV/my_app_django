from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return render(request, 'weather/index.html')

def get_weather(request):
    appid = '5d4b668bd4bc7e0c950cd5023dfe6473'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' +appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm() #прописываем для очистки формы от данных


    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        info = {'city': city.name,
            'temp': res['main']['temp'],
            'humidity': res['main']['humidity'],
            'icon': res['weather'][0]['icon'],
            'pressure': res['main']['pressure']
            }
        all_cities.append(info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/weather_1.html', context)
