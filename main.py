import streamlit as st
import translators as ts
from nltk.sentiment import SentimentIntensityAnalyzer


def translate_to_en(text):
    return ts.translate_text(text)


def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)["compound"]


st.title("Analiza Sentymentu")
st.write("Witaj! To jest strona do analizy sentymentu.")

user_input = st.text_area("Wprowadź tekst do analizy sentymentu:")

if st.button("Analizuj"):
    if user_input:
        sentiment_score = analyze_sentiment(translate_to_en(user_input))

        st.write("Wynik analizy sentymentu:", sentiment_score)

        if sentiment_score > 0:
            st.write("To pozytywny tekst!")
        elif sentiment_score < 0:
            st.write("To negatywny tekst.")
        else:
            st.write("To tekst neutralny.")
    else:
        st.warning("Wprowadź tekst przed analizą.")