import os
import requests

def get_weather_by_city(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("Failed to fetch weather data. Check your city name or API key.")

def get_weather_by_coordinates(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        
        print(f"Weather at coordinates ({lat}, {lon}):")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("Failed to fetch weather data. Check your coordinates or API key.")

if __name__ == "__main__":
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Use environment variable for security
    city = "Tashkent"  # Change this to your desired city
    get_weather_by_city(city, api_key)
    
    lat, lon = 41.2995, 69.2401  # Coordinates for Tashkent
    get_weather_by_coordinates(lat, lon, api_key)
