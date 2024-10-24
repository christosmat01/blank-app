import streamlit as st
import requests
from datetime import datetime

# OpenWeather API Key
API_KEY = '05436d09af0d5297d200a39bfb74d9ee'

# Sidebar navigation
st.sidebar.title("Weather Dashboard")
option = st.sidebar.selectbox(
    "Choose a widget",
    ("5-Day Weather Forecast", "Current Weather", "Other Widgets")
)

# Function to convert UTC time to readable format
def convert_time(utc_time):
    return datetime.utcfromtimestamp(utc_time).strftime('%Y-%m-%d %H:%M')

# Extract date from the timestamp
def get_day(utc_time):
    return datetime.utcfromtimestamp(utc_time).strftime('%Y-%m-%d')

# Widget 1: 5-Day Weather Forecast
if option == "5-Day Weather Forecast":
    city = "Athens"  # Replace this with any other city
    st.title(f'5-Day Weather Forecast for {city}')
    
    # Fetch the 5-day forecast from OpenWeather
    weather_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)
    weather_data = response.json()
    
    if response.status_code == 200:
        forecasts = weather_data['list']  # 5-day data (every 3 hours)
        
        # Dictionary to store one forecast per day
        daily_forecasts = {}

        # Loop through the forecasts and pick one forecast per day (e.g., at 12:00 PM)
        for forecast in forecasts:
            timestamp = forecast['dt']
            temp = forecast['main']['temp']
            weather_description = forecast['weather'][0]['description']
            weather_icon = forecast['weather'][0]['icon']
            weather_time = convert_time(timestamp)
            
            # Get the day of the forecast
            day = get_day(timestamp)
            
            # Select one forecast for each day (around 12:00 PM, or closest to it)
            hour = int(datetime.utcfromtimestamp(timestamp).strftime('%H'))
            if day not in daily_forecasts and 12 <= hour <= 15:  # Choose forecasts closest to noon
                daily_forecasts[day] = {
                    'time': weather_time,
                    'temp': temp,
                    'description': weather_description,
                    'icon': weather_icon
                }

        # Display the weather data for each day
        for day, forecast in daily_forecasts.items():
            st.write(f"**{forecast['time']}**")
            st.write(f"Temperature: {forecast['temp']}°C")
            st.write(f"Weather: {forecast['description']}")
            
            # Display the correct weather icon
            icon_url = f"http://openweathermap.org/img/wn/{forecast['icon']}@2x.png"
            st.image(icon_url, width=50)
    else:
        st.error("Failed to fetch weather data.")

# Widget 2: Current Weather (as an example for another widget)
elif option == "Current Weather":
    city = "Athens"
    st.title(f'Current Weather in {city}')
    
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(current_weather_url)
    current_weather_data = response.json()
    
    if response.status_code == 200:
        temp = current_weather_data['main']['temp']
        weather_description = current_weather_data['weather'][0]['description']
        weather_icon = current_weather_data['weather'][0]['icon']
        
        st.write(f"Temperature: {temp}°C")
        st.write(f"Weather: {weather_description}")
        
        # Display the weather icon
        icon_url = f"http://openweathermap.org/img/wn/{weather_icon}@2x.png"
        st.image(icon_url, width=50)
    else:
        st.error("Failed to fetch current weather data.")

# Placeholder for other widgets
elif option == "Other Widgets":
    st.title("Other Widgets will be displayed here")
