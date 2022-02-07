from django.urls import path
from .views import main

app_name = 'Main'

urlpatterns = [
    path('', main, name='Home')
]
