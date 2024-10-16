import streamlit as st
from google_trans_new import google_translator

try:
    # Initialize the translator
    translator = google_translator()

    # Text to be translated
    status = 'light rain'
    st.write(status)  # Display the original text

    # Translate the text from English (en) to Marathi (mr)
    translate_text = translator.translate(status, lang_src='en', lang_tgt='mr')

    # Display the translated text
    st.write(translate_text)
except Exception as e:
    st.write(f"An error occurred: {e}")