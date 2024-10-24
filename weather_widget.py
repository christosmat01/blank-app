import streamlit as st
import requests

def show_weather():
    # Function to get weather data
    def get_weather_data(city_name):
        api_key = "05436d09af0d5297d200a39bfb74d9ee"  # Replace with your OpenWeather API key
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        return data
    
    # City for which the weather will be displayed (can be fixed or dynamically selected)
    city_name = "Athens"  # Replace this with any default city or allow user input
    st.title(f"5-day Weather Forecast for {city_name}")
    
    weather_data = get_weather_data(city_name)
    
    if weather_data['cod'] == '200':
        for forecast in weather_data['list'][::8]:  # 3-hour intervals, selecting one per day
            date = forecast['dt_txt']
            temp = forecast['main']['temp']
            weather_desc = forecast['weather'][0]['description'].capitalize()
            icon_code = forecast['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            
            st.write(f"**Date:** {date}")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Weather:** {weather_desc}")
            st.image(icon_url)
            st.write("---")
    else:
        st.error("Error retrieving weather data. Please check the city name or your API key.")
