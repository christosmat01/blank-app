import streamlit as st
import requests

# OpenWeather API Key
API_KEY = '05436d09af0d5297d200a39bfb74d9ee'
LOCATION = 'Athens'

# Λειτουργία για να λαμβάνουμε δεδομένα καιρού
def get_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Ανάκτηση δεδομένων καιρού για την προκαθορισμένη τοποθεσία
weather_data = get_weather_data(LOCATION)

# Streamlit Web App
st.title("Current Weather Information")

if weather_data:
    st.write(f"Location: {weather_data['name']}")
    st.write(f"Temperature: {weather_data['main']['temp']} °C")
    st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
    st.write(f"Humidity: {weather_data['main']['humidity']}%")
    st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    st.error("Unable to retrieve weather data at the moment.")

