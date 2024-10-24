import streamlit as st
import requests

def show_exchange_rates():
    # Function to get exchange rates data
    def get_exchange_rates(base_currency):
        api_key = "9280aa1f7b95c1afd5828802"  # Use your own ExchangeRate-API key here
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        return data

    base_currency = "USD"  # Base currency can be changed dynamically if desired
    st.title(f"Exchange Rates for {base_currency}")
    
    exchange_data = get_exchange_rates(base_currency)
    
    if exchange_data['result'] == 'success':
        rates = exchange_data['conversion_rates']
        st.write(f"Base Currency: {base_currency}")
        st.write("---")
        st.write("Rates:")
        
        # Display top 10 currency rates
        top_10_currencies = list(rates.keys())[:10]
        for currency in top_10_currencies:
            st.write(f"{currency}: {rates[currency]}")
    else:
        st.error("Error retrieving exchange rates. Please check your API key or try again later.")
