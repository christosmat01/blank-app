import streamlit as st
import requests
from datetime import datetime

# OpenWeather API Key (replace with yours)
API_KEY = '05436d09af0d5297d200a39bfb74d9ee'

# Define the region/city
city = "Athens"  # Replace with your desired location

# OpenWeather API URL for 5-day forecast
weather_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'

# Fetch weather data from OpenWeather API
response = requests.get(weather_url)
weather_data = response.json()

# Convert UTC to local time
def convert_time(utc_time):
    return datetime.utcfromtimestamp(utc_time).strftime('%Y-%m-%d %H:%M:%S')

# Display Header
st.title(f'5-Day Weather Forecast for {city}')

# Display forecast for each of the next 5 days
if response.status_code == 200:
    for forecast in weather_data['list'][:5]:  # First 5 forecasts
        timestamp = forecast['dt']
        main_temp = forecast['main']['temp']
        weather_description = forecast['weather'][0]['description']
        weather_icon = forecast['weather'][0]['icon']
        weather_time = convert_time(timestamp)
        
        # Display the weather data with icons
        st.write(f"**{weather_time}**")
        st.write(f"Temperature: {main_temp} °C")
        st.write(f"Weather: {weather_description}")
        st.image(f"http://openweathermap.org/img/wn/{weather_icon}.png", width=50)
else:
    st.error("Failed to fetch weather data")
