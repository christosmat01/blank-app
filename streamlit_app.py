import streamlit as st
import requests
from datetime import datetime

# OpenWeather API Key (replace with yours)
API_KEY = '05436d09af0d5297d200a39bfb74d9ee'

# Define the city
city = "Athens"  # You can replace this with any other city

# Fetch the 5-day forecast from OpenWeather
weather_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
response = requests.get(weather_url)
weather_data = response.json()

# Display debugging information for weather data
st.write(f"Weather URL: {weather_url}")
st.write(f"Weather response status code: {response.status_code}")
st.write(f"Weather response data: {weather_data}")

# Convert UTC to local time
def convert_time(utc_time):
    return datetime.utcfromtimestamp(utc_time).strftime('%Y-%m-%d %H:%M')

# Display Header
st.title(f'5-Day Weather Forecast for {city}')

# Display forecast for the next 5 days
if response.status_code == 200:
    forecasts = weather_data['list']  # 5-day data (every 3 hours)

    for forecast in forecasts:
        timestamp = forecast['dt']
        temp = forecast['main']['temp']
        weather_description = forecast['weather'][0]['description']
        weather_icon = forecast['weather'][0]['icon']
        weather_time = convert_time(timestamp)
        
        # Display the weather data with icons
        st.write(f"**{weather_time}**")
        st.write(f"Temperature: {temp}°C")
        st.write(f"Weather: {weather_description}")
        
        # Display the correct weather icon
        icon_url = f"http://openweathermap.org/img/wn/{weather_icon}@2x.png"
        st.image(icon_url, width=50)
else:
    st.error("Failed to fetch weather data.")
