import pyfiglet
import requests
import re

#Weather API - weather stack

def setup():
    name = input('What is your name?')
def getIPWeather():
    ip = requests.get('http://ip.42.pl/raw').text
    response = requests.get('http://ip-api.com/json/'+ip).json()
    city = response['city']
    city = str(city).replace(" ", "%20")
    weather = requests.get('http://api.weatherstack.com/current?access_key=ef8b498ebf38e85990c49bcb3d4fc3b7&query='+city).json()
    print(weather)
    
with open('info.json') as f:
    if f.read() == '':
        setup()
        getIPWeather()
    else:
        getIPWeather()
