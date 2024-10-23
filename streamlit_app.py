import requests
import streamlit as st
import datetime

API_KEY = '05436d09af0d5297d200a39bfb74d9ee'
location = 'Limassol'

# URL για την πρόβλεψη καιρού για 5 ημέρες
forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"

def get_weather_forecast():
    response = requests.get(forecast_url)
    data = response.json()
    return data

def extract_forecast_data(weather_data):
    forecast_list = weather_data['list']
    forecast_data = []

    for forecast in forecast_list:
        dt = forecast['dt_txt']
        temperature = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        forecast_data.append({'datetime': dt, 'temp': temperature, 'description': description})

    return forecast_data

def display_forecast(forecast_data):
    st.title(f"5-Day Weather Forecast for {location}")

    # Εξαγωγή δεδομένων για τις επόμενες 5 ημέρες
    days = [datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S').date() for item in forecast_data]
    temps = [item['temp'] for item in forecast_data]
    descriptions = [item['description'] for item in forecast_data]

    # Εμφάνιση της θερμοκρασίας ως γραμμικό διάγραμμα
    st.line_chart(temps, width=700, height=400, use_container_width=False)
    
    # Εμφάνιση των περιγραφών καιρού σε πίνακα
    for day, temp, desc in zip(days, temps, descriptions):
        st.write(f"{day}: {temp}°C, {desc.capitalize()}")

weather_data = get_weather_forecast()
forecast_data = extract_forecast_data(weather_data)
display_forecast(forecast_data)
