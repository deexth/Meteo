from django.shortcuts import render
import os
import requests
from dotenv import load_dotenv
from .models import Weather
from .forms import MeteoForm

# Create your views here.
def index(request):
    load_dotenv()
    api_key = os.getenv('OPENWEATHER_API_KEY')
        
    if request.method == 'POST':
        form = MeteoForm(request.POST)
        form.save()
    form = MeteoForm()
    
    city = Weather.objects.all()
    meteo = []
    for c in city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={c}&units=metric&appid={api_key}'
        meteo_for_city = requests.get(url).json()
        meteo_dic = {
            'city': meteo_for_city['name'],	
            'temperature': meteo_for_city['main']['temp'],
            'description': meteo_for_city['weather'][0]['description'],
            'icon': meteo_for_city['weather'][0]['icon'],
        }
        meteo.append(meteo_dic)
    
    context = { 'meteo': meteo, 'form': form }	
    return render(request, 'meteo/index.html', context)