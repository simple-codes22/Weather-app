from django.shortcuts import render
import requests # The views will handle the json requests
import json
from .models import BASE_URL
from .testing import prototype

class Weather:
    API_KEY = "39d99238e9124fb4a5d150521220702"
    def get_current_weather(self, location='Paris'):
        """This gets the current location of a specific city"""
        req_ = requests.get(f"{BASE_URL}/current.json?key={self.API_KEY}&q={location}")
        response = json.loads(req_.content)
        return response

    def get_forecast(self, location='Paris'):
        """This produces the forecast of a city in the next five days"""
        req_ = requests.get(f"{BASE_URL}/forecast.json?key={self.API_KEY}&q={location}&days=5")
        response = json.loads(req_.content)
        return response

    def get_search_weather(self, location):
        """Whenever a user searches for a city, this function is used"""
        req_ = requests.get(f"{BASE_URL}/search.json?key={self.API_KEY}&q={location}")
        response = json.loads(req_.content)
        return response

def main(request, *args, **kwargs):
    if request.method == 'POST':
        pass
    return render(request, 'home.html', prototype)
# Create your views here.
