import streamlit as st
from libretranslatepy import LibreTranslateAPI

# Initialize the translator
translator = LibreTranslateAPI()

# Define the function to translate text
def translate_text(text, target_lang):
    try:
        translated = translator.translate(text, target_lang)
        return translated
    except Exception as e:
        return f"Translation failed: {e}"

# Streamlit app layout
st.title("LibreTranslate Translation App")

# Input field for text to translate
text_to_translate = st.text_area("Enter text to translate", "")

# Language selection dropdown
target_lang = st.selectbox(
    "Select target language",
    [
        ("Hindi", "hi"),
        ("Spanish", "es"),
        ("French", "fr"),
        ("German", "de"),
        ("Chinese", "zh"),
        ("Arabic", "ar"),
    ],
    format_func=lambda lang: lang[0],  # Display only language names
)

# Button to perform translation
if st.button("Translate"):
    if text_to_translate.strip():
        translated_text = translate_text(text_to_translate, target_lang[1])
        st.success(f"Translated Text: {translated_text}")
    else:
        st.error("Please enter text to translate.")