from django.shortcuts import render
from django.http import HttpResponse
import requests  
from .models import City
from .forms import CityForm
import pprint

def index(request): 
   #  city = 'Sonipat'   
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c5998eec66c9a2c6393237712b4cdc0d'
    
    err  = " "
    if request.method == 'POST':
       form = CityForm(request.POST)

       if form.is_valid():
          new_city = form.cleaned_data['name']
          
          max_count=City.objects.filter(name=new_city).count()
          
          if max_count==0:
             r = requests.get(url.format(new_city)).json()
             print(r)
             if r['cod'] == 200:
                form.save()
             else:
                err = "this not exist"



             
          else:
             err = " already exist"
      
    print(err)
      
          

    
       
         
        
    form = CityForm()


    cities = City.objects.all()

    weather_data = [ ]

    for city in cities:

      r = requests.get(url.format(city)).json()

      

      city_weather = {
         'city' :city.name,
         'temp' : r['main']['temp'],
         'description' :r['weather'][0]['description'],
         'icon' :r['weather'][0]['icon'],
      }


      weather_data.append(city_weather)
    print(weather_data)

    context = {'cityweather':  weather_data, 'form': form }

    return render(request, 'home.html', context)

    
