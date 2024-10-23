import streamlit as st
import requests

# API key και URL
API_KEY = "05436d09af0d5297d200a39bfb74d9ee"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Συνάρτηση για να πάρουμε δεδομένα καιρού
def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Δημιουργία dashboard στο Streamlit
def weather_widget():
    st.title("Weather Information")
    city = st.text_input("Enter the city", "Athens")  # Προεπιλογή στην Αθήνα
    if city:
        weather_data = get_weather(city)
        if weather_data:
            st.write(f"**City**: {weather_data['name']}")
            st.write(f"**Temperature**: {weather_data['main']['temp']}°C")
            st.write(f"**Weather**: {weather_data['weather'][0]['description'].capitalize()}")
        else:
            st.error("Error retrieving weather information")

if __name__ == "__main__":
    weather_widget()
