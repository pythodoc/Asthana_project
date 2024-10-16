import streamlit as st
from translate import Translator

# Initialize the translator with the target language (Marathi)
translator = Translator(to_lang='mr')

# Text to be translated
status = 'light rain'
st.write(status)  # Display the original text

# Translate the text
translate_text = translator.translate(status)

# Display the translated text
st.write(translate_text)