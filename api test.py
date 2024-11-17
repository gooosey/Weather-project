# Imports
import requests
import json

# Load API key from a file
with open('api_key.txt', 'r') as file:
    APIKey = file.read().strip()  # Read and remove any extra whitespace

# UserInputs
city = input()

# Initate url
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}"

# Grabbing data
try:
    # Asking for data 
    Response = requests.get(url)
    WeatherData = Response.json()

    Cityname = WeatherData['name']
    Citytemp = WeatherData['main']['temp']

    print(f'Weather for {Cityname}')
    print(f'Temp is {Citytemp}')


except requests.exceptions.RequestException as e:
    print("Check your internet")
    print(e)

except KeyError:
    print("try again")

    
