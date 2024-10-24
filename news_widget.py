import streamlit as st
import requests
from datetime import datetime, timedelta

def show_news():
    st.title("Latest News")

    # NewsAPI settings
    api_key = '3aebc5597a5c44cc853925ca704e4184'
    keyword = "technology"  # Λέξη-κλειδί για αναζήτηση ειδήσεων

    # Υπολογισμός της ώρας 2 ώρες πριν
    from_time = (datetime.utcnow() - timedelta(hours=2)).isoformat()

    # Κλήση στο NewsAPI για άρθρα που δημοσιεύτηκαν τις τελευταίες 2 ώρες
    url = f'https://newsapi.org/v2/everything?q={keyword}&from={from_time}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        articles = data.get('articles', [])

        if articles:
            st.subheader(f"Latest news about '{keyword}' from the last 2 hours")
            for article in articles[:10]: 
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')
                published_at = article.get('publishedAt')

                st.write(f"### {title}")
                st.write(f"*Published at:* {published_at}")
                st.write(f"{description}")
                st.write(f"[Read more]({url})")
                st.write("---")
        else:
            st.write(f"No news articles found for '{keyword}' in the last 2 hours.")
    else:
        st.error("Failed to retrieve news data.")
