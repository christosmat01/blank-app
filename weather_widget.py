import streamlit as st
import requests

def show_weather():
    st.title("Weather Forecast")
    
    # OpenWeather API settings
    api_key = '05436d09af0d5297d200a39bfb74d9ee'  # Use your OpenWeather API key
    city = "Limassol"  # Static city for now

    # Call the OpenWeather API for a 5-day forecast
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        st.subheader(f"5-Day Weather Forecast for {city}")
        for i in range(0, len(data['list']), 8):  # Get data for each day (8 intervals of 3 hours per day)
            day_data = data['list'][i]
            date = day_data['dt_txt'].split(" ")[0]
            temp = day_data['main']['temp']
            weather_description = day_data['weather'][0]['description']
            icon_code = day_data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            st.write(f"Date: {date}, Temp: {temp}°C, Description: {weather_description}")
            st.image(icon_url)
    else:
        st.error("Failed to retrieve weather data.")
