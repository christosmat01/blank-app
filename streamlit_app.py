import streamlit as st
from weather_widget import show_weather
from exchange_rates_widget import show_exchange_rates
from news_widget import show_news

# Sidebar setup
st.sidebar.title("Widgets Menu")

# Create a selection menu in the sidebar
option = st.sidebar.selectbox(
    'Select a widget to display:',
    ('Weather Information', 'Exchange Rates', 'Latest News')
)

# Display the selected widget based on user's choice
if option == 'Weather Information':
    show_weather()  # Calls the weather widget
elif option == 'Exchange Rates':
    show_exchange_rates()  # Calls the exchange rates widget
elif option == 'Latest News':
    show_news()  # Calls the latest news widget

# Optional: Footer or additional content can be added here
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by Your Name")
