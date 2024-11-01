import streamlit as st
import requests
from weather_widget import show_weather
from exchange_rates_widget import show_exchange_rates
from news_widget import show_news

# URLs for AWS Lambda endpoints
weather_lambda_url = "https://cxwrzdb4gopriy2b6gupooi7bi0pollw.lambda-url.eu-north-1.on.aws/"
exchange_lambda_url = "https://i5gcqqwgvpmqdxjpc57wghglle0xxjgs.lambda-url.eu-north-1.on.aws/"
news_lambda_url = "https://dzkk6m6fxh6kfzz2gdeqzafr5i0hogja.lambda-url.eu-north-1.on.aws/"

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
    show_weather()  # Calls the non-interactive weather widget
elif option == 'Exchange Rates':
    show_exchange_rates()  # Calls the non-interactive exchange rates widget
elif option == 'Latest News':
    show_news()  # Calls the non-interactive latest news widget

# Interactive weather widget
elif option == 'Interactive Weather Information':
    st.subheader("Interactive Weather Information")
    location = st.text_input("Enter the location for weather information:")
    
    if st.button("Get Weather"):
        # SEND: Sending a POST request to the weather Lambda function
        response = requests.post(weather_lambda_url, json={"queryStringParameters": {"location": location}})
        
        # RESPONSE: Handling the response
        if response.status_code == 200:
            data = response.json()
            st.write("Weather Information:")
            st.write(f"Location: {data['location']}")
            st.write(f"Temperature: {data['temperature']}°C")
            st.write(f"Condition: {data['condition']}")
        else:
            st.error(f"Failed to retrieve weather information. Status code: {response.status_code}")

# Interactive exchange rates widget
elif option == 'Interactive Exchange Rates':
    st.subheader("Interactive Exchange Rates")
    base_currency = st.text_input("Enter base currency (e.g., USD):")
    target_currency = st.text_input("Enter target currency (e.g., EUR):")
    
    if st.button("Get Exchange Rate"):
        # SEND: Sending a POST request to the exchange rates Lambda function
        response = requests.post(exchange_lambda_url, json={"queryStringParameters": {"base": base_currency, "target": target_currency}})
        
        # RESPONSE: Handling the response
        if response.status_code == 200:
            data = response.json()
            st.write("Exchange Rate Information:")
            st.write(f"Base Currency: {data['base_currency']}")
            st.write(f"Target Currency: {data['target_currency']}")
            st.write(f"Exchange Rate: {data['exchange_rate']}")
        else:
            st.error(f"Failed to retrieve exchange rate information. Status code: {response.status_code}")

# Interactive news widget
elif option == 'Interactive Latest News':
    st.subheader("Interactive Latest News")
    
    if st.button("Get Latest News"):
        # SEND: Sending a POST request to the news Lambda function
        response = requests.post(news_lambda_url, json={})
        
        # RESPONSE: Handling the response
        if response.status_code == 200:
            data = response.json()
            st.write("Latest News:")
            for article in data["articles"]:
                st.write(f"**{article['title']}**")
                st.write(f"{article['description']}")
                st.write(f"[Read more]({article['url']})")
        else:
            st.error(f"Failed to retrieve news information. Status code: {response.status_code}")
