import requests
from pprint import pprint

API_Key = '5ce57e537981fd1e858c3c867246f471'

city = input('Enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_Key + '&q=' + city

weather_data = requests.get(base_url).json()

print(weather_data)