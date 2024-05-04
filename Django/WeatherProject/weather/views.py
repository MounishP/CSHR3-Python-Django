from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6b59eab76101e1f5bbfe9ac7c53e2786")

        data = json.load(source)
        name=data['name']
        country = data['sys']['country']
        description=data['weather'][0]['description']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        temperature = data['main']['temp']-273.15
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']

        # print(name,description,latitude,longitude,temperature,pressure,humidity)

        dataOfWeather ={
            "name": name,
            "country": country,
            "description": description,
            "latitude":latitude,
            "longitude": longitude,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity
        }

        # print(dataOfWeather)

        # print(data)
        return render(request, 'index.html', dataOfWeather)
    return render(request, 'index.html')