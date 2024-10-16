import streamlit as st
from translate import Translator

# Initialize the translator with the target language (Marathi)
translator = Translator(to_lang='mr')

# Paragraph to be translated
paragraph = '''
The rain was light and steady, falling gently on the rooftops and trees. 
People walked through the streets with umbrellas, while children splashed 
in puddles, enjoying the cool breeze.
'''

st.write(paragraph)  # Display the original paragraph

# Translate the paragraph
translated_paragraph = translator.translate(paragraph)

# Display the translated paragraph
st.write(translated_paragraph))