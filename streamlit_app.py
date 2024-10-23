import streamlit as st
import requests
from datetime import datetime

# OpenWeather API Key (replace with yours)
API_KEY = '05436d09af0d5297d200a39bfb74d9ee'

# Define the region/city and fetch latitude/longitude
city = "Athens"  # Replace with your desired location
geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}'
geo_response = requests.get(geocode_url)
geo_data = geo_response.json()

if geo_response.status_code == 200 and len(geo_data) > 0:
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    # One Call API URL for 7-day forecast
    weather_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely,current,alerts&appid={API_KEY}&units=metric'
    
    # Fetch weather data
    response = requests.get(weather_url)
    weather_data = response.json()

    # Convert UTC to local time
    def convert_time(utc_time):
        return datetime.utcfromtimestamp(utc_time).strftime('%Y-%m-%d')

    # Display Header
    st.title(f'7-Day Weather Forecast for {city}')

    # Display forecast for the next 7 days
    if response.status_code == 200:
        daily_forecasts = weather_data['daily'][:7]  # First 7 days
        
        for forecast in daily_forecasts:
            timestamp = forecast['dt']
            max_temp = forecast['temp']['max']
            min_temp = forecast['temp']['min']
            weather_description = forecast['weather'][0]['description']
            weather_icon = forecast['weather'][0]['icon']
            weather_time = convert_time(timestamp)
            
            # Display the weather data with icons
            st.write(f"**{weather_time}**")
            st.write(f"Temperature: {min_temp}°C - {max_temp}°C")
            st.write(f"Weather: {weather_description}")
            
            # Display the correct weather icon
            icon_url = f"http://openweathermap.org/img/wn/{weather_icon}@2x.png"  # Using @2x for better resolution
            st.image(icon_url, width=50)
    else:
        st.error("Failed to fetch weather data")
else:
    st.error("Failed to retrieve geolocation data for the specified city.")
