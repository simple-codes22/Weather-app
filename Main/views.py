from django.shortcuts import redirect, render
from .models import Weather

MY_WEATHER = Weather()


def main(request="GET", current_location=MY_WEATHER.get_forecast('Lagos'), *args, **kwargs):
    if request.method == 'POST':
        geolocation = request.POST['geolocation']
        current_location = MY_WEATHER.get_forecast(geolocation)
    context = {
        'current': current_location['current'],
        'forecast': current_location['forecast'],
        'location': current_location['location'],
    }
    return render(request, 'home.html', context)
# Create your views here.
