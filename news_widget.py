import streamlit as st
import requests

def show_news():
    st.title("Latest News")

    # NewsAPI settings
    api_key = '3aebc5597a5c44cc853925ca704e4184'
    
    # URL για τα πιο πρόσφατα νέα
    url = f'https://newsapi.org/v2/top-headlines?language=en&apiKey={api_key}'

    # Κάνουμε την κλήση στο API
    response = requests.get(url)
    
    # Έλεγχος αν η κλήση ήταν επιτυχής
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        if articles:
            st.subheader(f"Most Recent News ({len(articles)} articles found)")
            for article in articles[:10]:  # Εμφανίζουμε τα πρώτα 10 άρθρα
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
            st.write("No recent news articles found.")
    else:
        st.error(f"Failed to retrieve news data. Status code: {response.status_code}")