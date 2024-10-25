import streamlit as st
import requests
from datetime import datetime

def show_weather():
    st.title("5-Day Weather Forecast")

    # OpenWeather API settings
    api_key = '05436d09af0d5297d200a39bfb74d9ee'
    city = "Athens"  # Μπορείς να αλλάξεις την πόλη

    # URL για να πάρουμε την 5-day forecast
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}'

    # Κάνουμε την κλήση στο API
    response = requests.get(url)
    
    # Έλεγχος αν η κλήση ήταν επιτυχής
    if response.status_code == 200:
        data = response.json()
        forecasts = data['list']
        
        # Εμφανίζουμε το όνομα της πόλης
        st.subheader(f"Weather Forecast for {city}")

        # Εμφανίζουμε την πρόβλεψη καιρού για 5 μέρες
        for forecast in forecasts[:5 * 8:8]:  # Λαμβάνουμε μόνο τα δεδομένα κάθε 24 ώρες
            timestamp = forecast['dt']  # UNIX timestamp
            date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  # Μετατροπή σε ημερομηνία και ώρα

            temp = forecast['main']['temp']
            weather_desc = forecast['weather'][0]['description']
            icon = forecast['weather'][0]['icon']

            st.write(f"### {date_time}")
            st.image(f"http://openweathermap.org/img/wn/{icon}.png")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Condition:** {weather_desc.capitalize()}")
            st.write("---")
    else:
        st.error(f"Failed to retrieve weather data. Status code: {response.status_code}")
