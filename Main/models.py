from django.db import models
import requests # The views will handle the json requests
import json

class Weather:
    BASE_URL = "https://api.weatherapi.com/v1" # Base url for the app
    API_KEY = "39d99238e9124fb4a5d150521220702"
    def get_current_weather(self, location='Paris'):
        """This gets the current location of a specific city"""
        req_ = requests.get(f"{self.BASE_URL}/current.json?key={self.API_KEY}&q={location}")
        response = json.loads(req_.content)
        return response

    def get_forecast(self, location='Paris'):
        """This produces the forecast of a city in the next five days"""
        
        req_ = requests.get(f"{self.BASE_URL}/forecast.json?key={self.API_KEY}&q={location}&days=5")
        response = json.loads(req_.content)
        return response

    def get_search_weather(self, location):
        """Whenever a user searches for a city, this function is used"""
        req_ = requests.get(f"{self.BASE_URL}/search.json?key={self.API_KEY}&q={location}")
        response = json.loads(req_.content)
        return response


condition_image = {
    "Sunny": "Utils/Sunny.svg",
    "Partly cloudy": "Utils/Sunny with cloud.svg",
    "Cloudy": "Utils/Cloudy Day.svg",
    "Overcast": "Utils/Sunny with cloud.svg",
    "Mist": "Utils/Sunny with mini rain.svg",
    "Patchy rain possible": "Utils/Sunny with rain 2.svg",
    "Patchy snow possible": "Utils/Snowy.svg",
    "Patchy sleet possible": "Utils/Snowy.svg",
    "Patchy freezing drizzle possible": "Utils/Rainy 1.svg",
    "Thundery outbreaks possible": "Utils/Stormy.svg",
    "Blowing snow": "Utils/Snowy.svg",
    "Blizzard": "Utils/Snowy.svg",
    "Fog": "Utils/Cloudy Day.svg",
    "Freezing Fog": "Utils/Snowy.svg",
    "Patchy light drizzle": "Utils/Rainy 2.svg",
    "Light drizzle": "Utils/Sunny with rain.svg",
    "Freezing drizzle": "Utils/Rainy 1.svg",
    "Heavy freezing drizzle": "Utils/Rainy 2.svg",
    "Patchy light rain": "Utils/Sunny with rain 2.svg",
    "Light rain": "Utils/Sunny with rain 2.svg",
    "Moderate rain at times": "Utils/Sunny with rain.svg",
    "Moderate rain": "Utils/Rainy 1.svg",
    "Heavy rain at times": "Utils/Rainy 2.svg",
    "Heavy rain": "Utils/Rainy 2.svg",
    "Light freezing rain": "Utils/Rainy 1.svg",
    "Moderate or heavy freezing rain": "Utils/Rainy 1.svg",
    "Light sleet": "Utils/Snowy.svg",
    "Moderate or heavy sleet": "Utils/Snowy.svg",
    "Patchy light snow": "Utils/Snowy.svg",
    "Light snow": "Utils/Snowy.svg",
    "Patchy moderate snow": "Utils/Snowy.svg",
    "Moderate snow": "Utils/Snowy.svg",
    "Patchy heavy snow": "Utils/Snowy.svg",
    "Heavy snow": "Utils/Snowy.svg",
    "Ice pellets": "Utils/Snowy.svg",
    "Light rain shower": "Utils/Cloudy Day.svg",
    "Moderate or heavy rain shower": "Utils/Rainy 2.svg",
    "Moderate or heavy snow shower": "Utils/Smowy.svg",
    "Torrential rain shower": "Utils/Rainy 2.svg",
    "Light sleet shower": "Utils/Snowy.svg",
    "Moderate or heavy sleet shower": "Utils/Snowy.svg",
    "Light snow shower": "Utils/Snowy.svg",
    "Moderate or heavy snow shower": "Utils/Snowy.svg",
    "Light showers of ice pellets": "Utils/Snowy.svg",
    "Moderate or heavy showers of ice pellets": "Utils/Snowy.svg",
    "Patchy light rain with thunder": "Utils/Stormy.svg",
    "Moderate or heavy rain with thunder": "Utils/Stormy.svg",
    "Patchy light snow with thunder": "Utils/Snowy.svg",
    "Moderate or heavy snow with thunder": "Utils/Snowy.svg",
    "Clear": "Utils/Nightly.svg"
}