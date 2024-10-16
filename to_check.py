from google_trans_new import google_translator

translator = google_translator()
st.write(status) #light rain 
translate_text = translator.translate(status, lang_tgt='mr')
st.write(translate_text) #chuva leve