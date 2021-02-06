import json
import pyfiglet
from os import system
import requests
import re

#Weather API - weather stack

name = ''
temperature = 0
feelsLike = 0
weatherDesc = ''

def setup():
    name = input('What is your name?')
    data = {}
    data['info'] = []
    data['info'].append({
        'name': name
    })
    with open('info.json','w') as infofile:
        json.dump(data, infofile)

def getIPWeather():
    ip = requests.get('http://ip.42.pl/raw').text
    response = requests.get('http://ip-api.com/json/'+ip).json()
    city = response['city']
    city = str(city).replace(" ", "%20")
    weather = requests.get('http://api.weatherstack.com/current?access_key=ef8b498ebf38e85990c49bcb3d4fc3b7&query='+city).json()
    print(weather)
    temperature = weather['current']['temperature']
    feelsLike = weather['current']['feelslike']
    weatherDesc = weather['current']['weather_descriptions']
    
with open('info.json') as f:
    if f.read() == '':
        setup()
        getIPWeather()
    else:
        getIPWeather()

system('clear')
ascii_banner = pyfiglet.figlet_format("Hello "+ name)
