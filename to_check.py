import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Text to be translated
status = 'light rain'
st.write(status)  # Display the original text

# Translate the text from English to Marathi (mr)
translated = translator.translate(status, src='en', dest='mr')

# Display the translated text
st.write(translated.text)