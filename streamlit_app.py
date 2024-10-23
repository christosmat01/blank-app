import json
import requests


def lambda_handler(event, context):
    API_KEY = "05436d09af0d5297d200a39bfb74d9ee"
    location = event.get("queryStringParameters", {}.get("location","Athens"))
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(weather_url)
    data = response.json()
    return data
