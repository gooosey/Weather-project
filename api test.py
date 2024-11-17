import requests
from datetime import datetime

# Load API key from a file
with open('api_key.txt', 'r') as file:
    APIKey = file.read().strip()

# User input for city name
city = input("Enter the city name: ")

# URL to get latitude and longitude (for accurate 7-day forecast API)
location_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}"
try:
    # Get coordinates for the city
    location_response = requests.get(location_url)
    location_response.raise_for_status()
    location_data = location_response.json()

    # Extract latitude and longitude
    lat = location_data['coord']['lat']
    lon = location_data['coord']['lon']

    # Now use the coordinates to get 7-day forecast
    forecast_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={APIKey}&units=metric"

    
    # Get forecast data
    forecast_response = requests.get(forecast_url)
    forecast_response.raise_for_status()
    forecast_data = forecast_response.json()

    # Extract daily temperatures and days of the week
    daily_data = forecast_data['daily']  # 7-day forecast data
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    print(f"Weather forecast for the next 7 days in {city}:")

    for i in range(7):
        day_timestamp = daily_data[i]['dt']
        day_name = days_of_week[datetime.utcfromtimestamp(day_timestamp).weekday()]
        temperature = round(daily_data[i]['temp']['day'])  # Day temperature in Celsius
        print(f"{day_name}: {temperature}°C")

except requests.exceptions.RequestException as e:
    print("Error fetching weather data. Check your internet or API key.")
    print(e)
except KeyError:
    print("Error parsing weather data. Ensure the city name is valid.")
