import streamlit as st
from translate import Translator
import requests
import json
import base64
import pandas as pd
from streamlit_player import st_player
import streamlit.components.v1 as components

lang_tgt= {'Marathi': 'mr', 'Hindi': 'hi', 'English': 'en'}

# Sidebar for language selection

selected_lang = st.sidebar.selectbox("Select Language", list(lang_tgt.keys()))

# Initialize the Translator
translator = Translator(to_lang=lang_tgt[selected_lang])

# Define paths for logos
main_logo_path = "logo.jpg"  # Replace with your main logo's path
sidebar_logo_path = "logo.jpg"  # Replace with your sidebar logo's path

# Sidebar logo
st.sidebar.image(sidebar_logo_path, width=200)  # Adjust width as needed


# Define translations for navigation items
nav_translations = {
    'Home': {'hi': 'होम', 'mr': 'होम'},
    'Gorakh Vani': {'hi': 'गोरखवाणी', 'mr': 'गोरखवाणी'},
    'Media Coverage': {'hi': 'मीडिया कव्हरेज', 'mr': 'मीडिया कव्हरेज'},
    'Nath Sampraday': {'hi': 'नाथ समुदाय', 'mr': 'नाथ संप्रदाय'},
    'About': {'hi': 'हमारे बारे में', 'mr': 'आमच्याबद्दल'},
    'Contact': {'hi': 'संपर्कं', 'mr': 'संपर्क'},
    'Resources': {'hi': 'संसाधन', 'mr': 'संसाधन निवडा'},
    'Registration': {'hi': 'पंजीकरण', 'mr': 'नोंदणी'},
    #"Select a resource": {'hi':'संसाधन चुनें',"mr": "संसाधन निवडा"},
    #"Nath Bhajan": {'hi':'नाथ भजन',"mr": "नाथ भजन"},
    #"Articles": {'hi':'सामग्री',"mr": "लेख"},
    #"Books": {'hi':'पुस्तके',"mr": "पुस्तके"}
}

# Translate navigation items based on the selected language
translated_nav = {item: nav_translations[item].get(lang_tgt[selected_lang], item) for item in nav_translations.keys()}


# Add the navigation items to the sidebar
page = st.sidebar.radio("Navigate", list(translated_nav.values()))

# Function to translate text
def translate_text(text):
    try:
        translated = translator.translate(text)
        return translated
    except Exception as e:
        st.error(f"Translation failed: {e}")
        return text

# Display content based on the selected page
if page in ["Home", "होम", "होम"]:
    
    # Top content: text and social media icons
    st.markdown("""
        
        <div>
            <h2>ॐ शिव गोरक्ष योगी अस्थाना.(आटगाव)</h2>
            <p>ऊँ नमो भगवते गोरक्षनाथाय | धर्मो रक्षति रक्षितः | श्री गोरक्षनाथो विजयतेतराम | यतो धर्मस्ततो जयः |</p>
        </div>""", unsafe_allow_html=True)
        
    banner_html = """
<div class="slideshow-container">

  <!-- First Image -->
  <div class="mySlides fade">
    <img src="https://via.placeholder.com/800x300?text=First+Image" style="width:100%">
  </div>

  <!-- Second Image -->
  <div class="mySlides fade">
    <img src="https://via.placeholder.com/800x300?text=Second+Image" style="width:100%">
  </div>

  <!-- Third Image -->
  <div class="mySlides fade">
    <img src="https://via.placeholder.com/800x300?text=Third+Image" style="width:100%">
  </div>

</div>

<style>
.slideshow-container {
  position: relative;
  max-width: 1000px;
  margin: auto;
}

.mySlides {
  display: none;
}

.fade {
  animation-name: fade;
  animation-duration: 2.5s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
</style>

<script>
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  slides[slideIndex-1].style.display = "block";  
  setTimeout(showSlides, 3000); // Change image every 3 seconds
}
</script>
"""
#if page in ["Home", "होम", "होम"]:
   # display_Home()

# Embed the HTML and CSS in the Streamlit app
    st.markdown(banner_html, unsafe_allow_html=True)

    # Create two columns: one for the image and one for the details
    col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed

    # Display the image in the left column
    with col1:
        st.image('shri guruji.PNG', use_container_width=True)

    # Display the details in the right column
    with col2:
        st.header("श्री गुरुजी नाथभक्त तुषार वेखंडे.(श्री रविशनाथ जी)")
        st.write("""ऊँ शिव गोरक्ष योगी अस्थाना (आटगाव)""")

        # Instagram profile URL
        instagram_url = "https://www.instagram.com/tushar_vekhande_patriot/"

        # YouTube channel URL
        youtube_url = "https://www.youtube.com/@tushar_vekhande"

        # Facebook profile URL
        facebook_url = "https://www.facebook.com/tushar.vekhande"

        # Instagram logo URL
        instagram_logo_url = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"

        # YouTube logo URL (alternative)
        youtube_logo_url = "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg"

        # Facebook logo URL
        facebook_logo_url = "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"

        # Create clickable icons side by side
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 10px;">
                <a href="{instagram_url}" target="_blank">
                    <img src="{instagram_logo_url}" alt="Instagram" style="width:50px;height:50px;">
                </a>
                <a href="{youtube_url}" target="_blank">
                    <img src="{youtube_logo_url}" alt="YouTube" style="width:50px;height:50px;">
                </a>
                <a href="{facebook_url}" target="_blank">
                    <img src="{facebook_logo_url}" alt="Facebook" style="width:50px;height:50px;">
                </a>
            </div>
            """, unsafe_allow_html=True)
        
    # Second row: Content on the left, image on the right
    col3, col4 = st.columns([2, 1])

    with col3:
        st.header("श्री श्री श्री दादागुरु सतनाथ जी महाराज(औघड पीर)")
        st.write("""
           ऊँ शिव गोरक्ष योगी अस्थाना (चितेगाव)
        """)

    with col4:
        st.image('dadaguru.PNG', use_container_width =True)
# Handle dropdown selection separately
#elif page in ["Resources","संसाधन","संसाधने"]:
    #resource_selection = st.selectbox("Select a resource", ["Bhakti Geet", "Articles", "Books"])
    #page = resource_selection  # Override page with selected resource
elif page in ["About", "हमारे बारे में", "आमच्याबद्दल"]:
    #header = "ॐ शिव गोरक्ष योगी अस्थाना.(आटगांव)"
    #maps_link = "https://maps.app.goo.gl/2popDrBbygVPard36"
    #st.markdown(f"[Open Location in Google Maps]({maps_link})")
    content = """
        ॐ shiv goraksha yogi dhunaa kuti
        
        1. Nath Seva
        2. Gou Raksha
        3. Educational Help for Needy Children
        4. Dharma Raksha     
    """
    #def google_map(center_lat, center_lon):
    
    latitude = 19.5059314
    longitude = 73.3245044

# Create a DataFrame with the coordinates
    data = pd.DataFrame({
        'lat': [latitude],
        'lon': [longitude]
    })

# Display the map
    st.title("ॐ शिव गोरक्ष योगी अस्थाना. (आटगांव)")
    st.map(data)

    #translated_header = translate_text(header)
    translated_content = translate_text(content)
    #st.header(translated_header)
    st.write(translated_content)
elif page in ["Contact", "संपर्क"]:
    header = "Contact Us"
    content = """
        All Guru bandhu's are for your help please find our shisya mandal as per District wise in address section
    """
    translated_header = translate_text(header)
    translated_content = translate_text(content)
    st.header(translated_header)
    st.write(translated_content)
    df=pd.read_csv("registration_data.csv")   
    st.write(df)
elif page in ['Gorakh Vani', 'गोरखवाणी', 'गोरखवाणी']:
    header = "Gorakh Vani"

    content = """

**सति सति बोले गोरख राणा
तीनि चरन का संग निवारी सकता बूझा कारण॥**

'गोरखनाथ अब यह अनुभव सिद्ध मन्त्र कहत हैं, कि तीन तरी (तीनों त्रस्त्र), जागरण आदि छः चार तेज जो कर्मपद में जीवन धारक होत, 
सो अयोध्याधिराज संयम के नियम विवर्ण बलह, क्योंकि वे जीवन हेतना-हौसा की पीड़िता होने के कारण हरण कर सकते हैं, 
अर्थात वे निश्चित विवर्णन-प्रभावी होते हैं।'

**कहि न सोहै सूरतिन समयलब्ध के साधिया
जब तक करकट लगावैति काली हठी हारिया**

'रति का संग समयलभाद के द्वारा 'गुरुचरण' मार्ग उच्चारित होता है। यह निर्मलता है कि समाज में, अनुभवित (शक्ति), 
संवेदनशीलता और संबंधों की सूझ होती है। यही सत्य है कि अज्ञानता के ग्रहण से हठियों में निराशा का उद्भव होता है, अकारण में हार का परिणाम और अंततः रति।

संपूर्ण शरीर के साथ सूरतिन में सत्य के मार्ग में चित्त स्थिरता और विशुद्धता के नियमों के अंतर्गत केवल वही सजीव होता है, 
जो हठ से निजात पाकर संयम, अति संयम के विशेष ज्ञान को प्राप्त कर सकता है। विवेक और जीवन की आध्यात्मिक सिद्धि में चित की स्थिरता और सन्तुलन जीवंत रहता है।'
    """
    translated_header = translate_text(header)
    # translated_content = translate_text(content)
    st.header(translated_header)
    st.write(content)
elif page in ["Media Coverage", "मीडिया कव्हरेज", "मीडिया कव्हरेज"]:
    header = "Media Coverage"
    content = """
        this is sample
    """
    st_player("https://www.youtube.com/playlist?list=PL6uoWbCpalBCr5BMGH-GmAqxuLdq_lkYr&si=AqvcauntO-igSXTW")
    translated_header = translate_text(header)
    translated_content = translate_text(content)
    st.header(translated_header)
    st.write(translated_content)
elif page in ["Nath Sampraday", "नाथ समुदाय", "नाथ संप्रदाय"]:
    st.image(r'Shiv Gorakshanath.jpeg')


    header = "Nath Panth"
    content = """
 The Nath tradition, also known as the Nath Panth, is a spiritual movement that originated in India in the 9th century. It is a lineage of spiritual teachers and gurus who are believed to have extraordinary powers and abilities and are respected as custodians of ancient knowledge and wisdom. The Nath tradition is deeply rooted in Hindu mythology and is associated with 9 Naths, a group of powerful saints who are said to have been born out of the divine energy of Lord Shiva.

The Nath tradition is known for its emphasis on attaining spiritual knowledge through yoga, meditation and realization of the ultimate reality. This tradition is based on the principles of Hatha Yoga, which include physical posture, breathing techniques and the practice of meditation to achieve spiritual growth and self-realization. The Nath tradition is also associated with the Kundalini energy system, which is a complex network of energy centers in the body that is believed to be responsible for spiritual progress and transformation.

According to legend, the Nath tradition was founded by Matsyendranath, the first of the 9 Naths, who is said to have lived in the 9th century. Matsyendranath is credited with developing the principles of Hatha Yoga and Kundalini energy systems and is believed to have written several books on yoga and spirituality, including Kaul Gyan Nirnay and Jnana Sankalini Tantra. He is said to have established the first Nath Math in the city of Qadri in the Indian state of Karnataka.

The Nath tradition is known for its emphasis on the guru-shishya tradition, where the spiritual teacher or guru guides and initiates the disciple on the path of spiritual advancement and self-realization. The Guru is believed to have the power to transmit spiritual energy and knowledge to the disciple and is considered a symbol of God. The Nath tradition is also associated with the concept of Shaktipat or the concept of communication of spiritual energy from guru to disciple, which is considered essential for spiritual progress and transformation.

The Nath tradition has a rich and diverse history, with many notable gurus and spiritual teachers contributing to its development and growth. One of the most important gurus in the Nath tradition is Gorakhnath, who lived in the 11th century and is credited with developing the principles of yoga and meditation. Gorakhnath is believed to have written several books on yoga and spirituality, including the Goraksha Samhita and Siddha Siddhanta Padhati, and is considered one of the most important gurus in the Nath tradition.

As there are twelve Panth as follows in above image
    """
    # URL of the image
    image_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-tzwVAQFGSWmqqehtJ48QBf4_jrcoiVegZtHML7XHfLwu4mA6ozr560QMnkmDVpY0nAewUn7G2Mftq4VAcTtwdwaaEKkkkAV4d54wbwi8fqhFi4hznohcxTxRNIph9XtITmYYreFjvTI/s1600/Nath+Cult_Top+Yoga+Alert_Lord+Shiva_Guru+Gorakhnath_Gangai_Nath.jpg"  # Replace with your image URL

    # Display the image using st.markdown
    st.markdown(f'<img src="{image_url}" alt="Image" style="width:100%;"/>', unsafe_allow_html=True)
    #st.markdown(r'C:\Users\Admin\Desktop\Asthana Proj\all_panth1.jpg')
    translated_header = translate_text(header)
    translated_content = translate_text(content)
    st.header(translated_header)
    st.write(translated_content)
elif page in ['Registration', "पंजीकरण", "नोंदणी"]:
    df = pd.DataFrame(columns=["Name", "Email", "Phone", "Address", "Gender", "Age"])
    title = "Registration Form"
    content = """
    1. Your Name
    2. E-Mail
    3. Contact Number
    4. Address
    5. Gender
    6. Age
    7. Terms and Conditions
    """
    
    # Translated title
    translated_title = translate_text(title)
    st.title(translated_title)

    # Registration form fields
    name = st.text_input(translate_text("Your's Name"))
    email = st.text_input(translate_text("E-Mail"))
    phone = st.text_input(translate_text("Contact Num"))
    address = st.text_area(translate_text("Address"))

    # Gender selection
    gender = st.radio(translate_text("Gender"), ("पुरुष", "स्त्री"), horizontal=True)

    # Age input
    age = st.number_input(translate_text("Age"), min_value=18, max_value=100)

    # Terms and conditions checkbox
    agree = st.checkbox(translate_text("I agree to the Terms and Conditions."))
    
    file_path = "registration_data.csv"
    
    # Validation and submission
    if st.button("Submit"):
        if not name:
            st.error(translate_text("Please enter your name."))
        elif not email:
            st.error(translate_text("Please enter your E-Mail."))
        elif not phone:
            st.error(translate_text("Please enter your contact number."))
        elif not address:
            st.error(translate_text("Please enter your address."))
        elif not agree:
            st.error(translate_text("For registration, please accept the terms and conditions."))
        else:
            new_data = pd.DataFrame(
                {"Name": [name], "Email": [email], "Phone": [phone], "Address": [address], "Gender": [gender],
                 "Age": [age]})
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(file_path, index=False)
            st.success(f"Thank you, {name}! Your form has been submitted successfully.")

elif page in["Resources","संसाधन","संसाधने"]:  # Use the translated "Resources" label
    resource_selection = st.selectbox(translate_text("Select a resource", ["Nath Bhajan", "Articles", "Books"]))
    if resource_selection == "Videos":
        header = "Resources - Videos"
        content = "Content for videos"
        # Translate the header and content
        translated_header = translate_text(header)
        translated_content = translate_text(content)
        st.header(translated_header)
        st.write(translated_content)
    elif resource_selection == "Articles":
        header = "Resources - Articles"
        content = "Content for articles"
        # Translate the header and content
        translated_header = translate_text(header)
        translated_content = translate_text(content)
        st.header(translated_header)
        st.write(translated_content)
    elif resource_selection == "Books":
        header = "Resources - Books"
        content = "Content for books"
        # Translate the header and content
        translated_header = translate_text(header)
        translated_content = translate_text(content)
        translated_resource=translate_text(resource_selection)
        st.header(translated_header)
        st.write(translated_content)
        st.write(translated_resource)
else:
    header = "Page Not Found"
    content = "The page you are looking for does not exist."
    translated_header = translate_text(header)
    translated_content = translate_text(content)
    #translated_resource=translate_text(resource_selection]+
    st.header(translated_header)
    st.write(translated_content)
        #st.write(translated_resource)
    
    
