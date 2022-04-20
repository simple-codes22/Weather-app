from django.shortcuts import redirect, render
from .models import Weather, condition_image
from django.templatetags.static import static

MY_WEATHER = Weather()



def main(request="GET", current_location=MY_WEATHER.get_forecast('Lagos'), *args, **kwargs):
    if request.method == 'POST':
        geolocation = request.POST['geolocation']
        current_location = MY_WEATHER.get_forecast(geolocation)
    
    current_condition = current_location['current']['condition']['text']
    condition_forecast_src = [static(condition_image[days['day']['condition']['text']]) for days in current_location['forecast']['forecastday']]
    
    context = {
        'current': current_location['current'],
        'forecast': current_location['forecast'],
        'location': current_location['location'],
        'today_image': static(condition_image[current_condition]),
        'forecast_image': condition_forecast_src,
    }
    return render(request, 'home.html', context)

