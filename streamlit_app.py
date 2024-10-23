import requests
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Your OpenWeather API key
API_KEY = '05436d09af0d5297d200a39bfb74d9ee'

# Location for weather
location = 'Athens'

# URL for the 5-day weather forecast
forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"

# Function to get weather forecast data
def get_weather_forecast():
    response = requests.get(forecast_url)
    data = response.json()
    return data

# Extract forecast data
def extract_forecast_data(weather_data):
    forecast_list = weather_data['list']
    forecast_data = []

    for forecast in forecast_list[:10]:  # Get the first 10 forecasts (for example purposes)
        dt = forecast['dt_txt']
        temperature = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        icon = forecast['weather'][0]['icon']  # Weather icon
        forecast_data.append({
            'datetime': dt, 
            'temp': temperature, 
            'description': description,
            'icon': icon
        })

    return forecast_data

# Function to display the forecast in a visual form
def display_forecast(forecast_data):
    # Create plot
    fig = go.Figure()

    # Add temperature line
    temps = [item['temp'] for item in forecast_data]
    times = [item['datetime'] for item in forecast_data]
    
    fig.add_trace(go.Scatter(x=times, y=temps, mode='lines', name='Temperature'))

    # Add weather icons
    for i, item in enumerate(forecast_data):
        icon_url = f"http://openweathermap.org/img/wn/{item['icon']}@2x.png"  # Weather icon URL
        fig.add_layout_image(
            dict(
                source=icon_url,
                x=i,  # Position on x-axis
                y=item['temp'] + 1,  # Position on y-axis, just above temperature
                xref="x",
                yref="y",
                sizex=0.1,
                sizey=0.1,
                xanchor="center",
                yanchor="bottom"
            )
        )

    # Update layout for better visuals
    fig.update_layout(
        title=f"5-Day Weather Forecast for {location}",
        xaxis_title="Date and Time",
        yaxis_title="Temperature (°C)",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig)

# Get weather data
weather_data = get_weather_forecast()

# Extract relevant forecast data
forecast_data = extract_forecast_data(weather_data)

# Display forecast
display_forecast(forecast_data)
