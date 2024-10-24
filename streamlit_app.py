import streamlit as st
import requests
from datetime import datetime

# Sidebar for widget selection
st.sidebar.title("Widgets")
option = st.sidebar.selectbox(
    "Choose a widget to view",
    ["Weather Information", "Exchange Rates", "Latest News"]
)

# Function to get weather data
def get_weather_data(city):
    api_key = "05436d09af0d5297d200a39bfb74d9ee"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    forecast_data = []
    for forecast in data['list']:
        date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d %H:%M:%S')
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        icon = forecast['weather'][0]['icon']
        forecast_data.append((date, temp, description, icon))
    
    return forecast_data, data['city']['name']

# Display weather data
if option == "Weather Information":
    city = "London"  # You can change this to any city you want.
    st.title(f"5-Day Weather Forecast for {city}")

    weather_data, city_name = get_weather_data(city)
    
    for date, temp, description, icon in weather_data[::8]:  # Every 8th entry (24-hour intervals)
        st.write(f"Date: {date}")
        st.write(f"Temperature: {temp}°C")
        st.write(f"Description: {description}")
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        st.write("---")

# Placeholder for Exchange Rates widget
if option == "Exchange Rates":
    st.title("Exchange Rates Widget (coming soon...)")

# Placeholder for Latest News widget
if option == "Latest News":
    st.title("Latest News Widget (coming soon...)")
