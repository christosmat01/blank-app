import streamlit as st
import requests
from weather_widget import show_weather
from exchange_rates_widget import show_exchange_rates
from news_widget import show_news

# URLs for AWS Lambda endpoints
weather_lambda_url = "https://8y2jj2g2kk.execute-api.eu-north-1.amazonaws.com/weather"
exchange_lambda_url = "https://8y2jj2g2kk.execute-api.eu-north-1.amazonaws.com/exchange"
news_lambda_url = "https://8y2jj2g2kk.execute-api.eu-north-1.amazonaws.com/news"

# Sidebar setup
st.sidebar.title("Widgets Menu")

# Create a selection menu in the sidebar
option = st.sidebar.selectbox(
    'Select a widget to display:',
    ('Weather Information', 'Exchange Rates', 'Latest News', 
     'Interactive Weather Information', 'Interactive Exchange Rates', 'Interactive Latest News')
)

# Display the selected widget based on user's choice
if option == 'Weather Information':
    show_weather()  # Calls the weather widget
elif option == 'Exchange Rates':
    show_exchange_rates()  # Calls the exchange rates widget
elif option == 'Latest News':
    show_news()  # Calls the latest news widget

# Interactive weather widget
elif option == 'Interactive Weather Information':
    location = st.text_input("Enter the location for weather information:")
    if st.button("Get Weather"):
        response = requests.get(f"{weather_lambda_url}?location={location}")
        if response.status_code == 200:
            data = response.json()
            st.write(f"### Weather Information for {location}:")
            st.write(f"**Temperature:** {data['temperature']}°C")
            st.write(f"**Humidity:** {data['humidity']}%")
            st.write(f"**Condition:** {data['weather']}")
            st.write("**Forecast:**")
            for forecast in data.get("forecast", []):
                st.write(f"- **{forecast['day']}:** {forecast['temperature']}°C, {forecast['condition']}")
        else:
            st.error(f"Failed to retrieve weather information. Status code: {response.status_code}, Error: {response.text}")

# Interactive exchange rates widget
elif option == 'Interactive Exchange Rates':
    base_currency = st.text_input("Enter base currency (e.g., USD):")
    target_currency = st.text_input("Enter target currency (e.g., EUR):")
    if st.button("Get Exchange Rate"):
        response = requests.post(exchange_lambda_url, json={"base": base_currency, "target": target_currency})
        if response.status_code == 200:
            data = response.json()
            st.write(f"### Exchange Rate from {base_currency} to {target_currency}")
            st.write(f"**1 {base_currency}** = {data['exchange_rate']} {target_currency}")
        else:
            st.error(f"Failed to retrieve exchange rate information. Status code: {response.status_code}, Error: {response.text}")

# Interactive news widget
elif option == 'Interactive Latest News':
    if st.button("Get Latest News"):
        response = requests.post(news_lambda_url, json={})
        if response.status_code == 200:
            data = response.json()
            st.write("### Latest News:")
            for article in data.get("articles", []):
                st.write(f"**{article['title']}**")
                st.write(f"{article['description']}")
                st.write(f"[Read more]({article['url']})")
                st.write("---")  # Divider between articles for clarity
        else:
            st.error(f"Failed to retrieve news information. Status code: {response.status_code}, Error: {response.text}")
