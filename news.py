import streamlit as st
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='421a63a7ccbf49408a4e4d8e80cc5c6a')


# Sidebar options
st.sidebar.title("News Categories")
categories = st.sidebar.radio("Select a category:", ['business', 'entertainment', 'health', 'science', 'sports', 'technology'])

# Define country codes and full country names
country_options = {
    'us': 'United States',
    'gb': 'United Kingdom',
    'in': 'India',
    'au': 'Australia',
    'ca': 'Canada',
    'fr': 'France',
    'de': 'Germany',
    'jp': 'Japan',
    'it': 'Italy',
    'nl': 'Netherlands',
    'nz': 'New Zealand',
    'ru': 'Russia',
    'sa': 'Saudi Arabia',
    'sg': 'Singapore',
    'za': 'South Africa',
    'kr': 'South Korea',
    'se': 'Sweden',
    'ch': 'Switzerland',
    'ae': 'United Arab Emirates',
    'cn': 'China'
}

# Select country
country = st.sidebar.selectbox("Select a country:", list(country_options.keys()), format_func=lambda x: country_options[x])

# Select number of articles
num_articles = st.sidebar.slider("Select number of articles:", 1, 30, 10)

# Fetch news articles based on selected category, country, and number of articles
articles = newsapi.get_top_headlines(category=categories, language='en', country=country, page_size=num_articles)

# Search box
search_query = st.sidebar.text_input("Search for articles")

# Filter articles based on search query
filtered_articles = []
if search_query:
    filtered_articles = [article for article in articles['articles'] if search_query.lower() in article['title'].lower()]
else:
    filtered_articles = articles['articles']

# Display article details
st.title("News Aggregator App")
st.subheader(f"Top {num_articles} headlines in {categories.capitalize()} category from {country_options[country]}:")

for article in filtered_articles:
    st.write('---')
    st.write(f"**Title:** {article['title']}")
    st.write(f"**Author:** {article['author']}")
    st.write(f"**Published At:** {article['publishedAt']}")
    st.write(f"**Description:** {article['description']}")
    st.write(f"**Source:** {article['source']['name']}")
    st.write(f"**URL:** [{article['url']}]({article['url']})")












