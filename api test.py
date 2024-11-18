# Imports
import requests
import json

# Dont look at my API please
with open('api_key.txt', 'r') as file:
    APIKey = file.read().strip() 

# UserInputs
city = input()

# Initate url
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}&units=metric"

# Grabbing data
try:
    # Asking for data 
    Response = requests.get(url)
    WeatherData = Response.json()

    Cityname = WeatherData['name']
    Citytemp = WeatherData['main']['temp']

    print(f'Weather for {Cityname}')
    print(f'Temp is {Citytemp}C')


except requests.exceptions.RequestException as e:
    print("Check your internet")
    print(e)

except KeyError:
    print("try again")

    
