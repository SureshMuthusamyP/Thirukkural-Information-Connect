import streamlit as st
import pandas as pd
from utility import search_thirukkural



def main():
    # Custom styling
    st.markdown(
        """
        <style>
            .container {
                border: 1px solid #ffffff;
                padding: 15px;
                border-radius: 10px;
                margin-top: 20px;
                margin-bottom: 20px;
                white-space: pre-wrap;
            }
            
            .container-header {
                color: #ffffff;
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
                background-color: #333333;
                padding: 5px;
                border-radius: 5px;
                text-align: center;
            }
            
            .key {
                color: #ffffff;
                font-weight: bold;
            }
            
            .center-text {
                text-align: center;
            }

            .content {
                font-size: 16px;  /* Adjust the font size as needed */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    
    selected_language = st.selectbox("**தேர்வு மொழி/Preferred Language/पसंदीदा भाषा:**", ['தமிழ்', 'English', 'हिन्दी'])
    image_path = "thiruvalluvar.jpg"
    st.sidebar.image(image_path, caption="திருவள்ளுவர்/Thiruvalluvar/तिरुवल्लुवर", width=280)


    # Language selection dropdown
    if selected_language == 'தமிழ்':
       st.title("திருக்குறள் தகவல் இணைப்பு")
       user_input = st.text_input("திருக்குறளை உள்ளிடவும்")
       data = {
       'விளக்கம்': ['பால்', 'இயல்', 'அதிகாரம்', 'குறள்'],
       'எண்ணிக்கை': [3, 13, 133, 1330]
}
       side_table = pd.DataFrame(data)
       st.sidebar.header("திருக்குறளின் வரலாறு")
       st.sidebar.markdown("திருக்குறள் சங்க காலத்தைச் சேர்ந்த இலக்கியம். இந்த இலக்கியம் பதினென்கீழ்க்கனக்கு எனப்படும், பதினெட்டு நூல்களில் ஒன்று. திருக்குறள் என்பது இவ்விலக்கியத்தின் இயற்ப்பெயர் அல்ல. இவ்விலக்கியத்தில் உள்ள பாடல்கள் குறள் வெண்பா மரபில் உள்ளதால், திருக்குறள் என்ற பெயர் பெற்றது.")
       st.sidebar.markdown(" இந்தப் படைப்பில் ஒரு பகுதியே கிடைத்ததாக கூறப்படுகிறது. அவை கீழே கூறியபடி 1330 குறள்கள் கொண்டது. இந்த படைப்பை இயற்றியவரின் பெயர் உறுதியாக கண்டறியவில்லை. இதுவரை சேகரித்த தகவல்படி வள்ளுவ மரபைச் சேர்ந்தவர் என்பதால் திருவள்ளுவர் என்ற பெயர் பெற்றார்")
       st.sidebar.table(side_table)
    elif selected_language == 'English':
        st.title("Thirukkural Information Connect")
        user_input = st.text_input("Enter the Thirukkural:")
        data = {
    'Description': ['Division', 'Book', 'Chapter', 'Couplets'],
    'Count': [3, 13, 133, 1330]
}
        side_table = pd.DataFrame(data)
        st.sidebar.header("Thirukkural History")  
        st.sidebar.markdown("Thirukkural literature belongs to the Sanga Tamil period,written in Tamil language. This literature is part of the Pathinen Keezhkanaku set of books. Thirukkural is not the original/real name of this work, this literature is made of couplets style poems.Based on this, and to give respectful prefix made the name Thirukkural [Thiru - respectful part in tamil language + Kural -couplet)]. ")
        st.sidebar.markdown("Researchers claim that work those are discovered (until now) are just a part of the much larger one, the discovered/restored work consists of 1330 couplets. Name of the Author of this work is not known either. Based on the information found so far, its discovered a person who belonged to Valluva tradition could be the author. That resulted in the name as Thiruvalluvar [Thiru + Valluvar].")
        st.sidebar.table(side_table)
    elif selected_language == 'हिन्दी':
        st.title("थिरुक्कुरल जानकारी कनेक्ट")
        user_input = st.text_input("तिरुकुरल डालें")
        data = {
    'विवरण': ['कांड', 'हिस्सा', 'अध्याय', 'कुरल'],
    'गिनती': [3, 13, 133, 1330]
}
        
        side_table = pd.DataFrame(data)
        st.sidebar.header("थिरुक्कुरल् इतिहास")
        st.sidebar.markdown("थिरुक्कुरल् साहित्य  तमिल की अवधि के लिए , तमिल  भाषा में लिखा गया के अंतर्गत आता है। इस साहित्य पुस्तकों का सेट है  का हिस्सा है। इस काम के मूल/वास्तविक नाम नहीं है, इस साहित्य की शैली शायरी कविताएँ (बना दिया है। इस पर, और सम्मानजनक उपसर्ग नाम थिरुक्कुरल् बना देने के लिए आधार [थिरू ( तमिल भाषा में सम्मानजनक भाग)  शेर)]।")
        st.sidebar.markdown("शोधकर्ताओं का दावा है कि काम उन लोगों (अब तक) की खोज कर रहे हैं बस एक बहुत बड़ा का एक हिस्सा हैं, पता चला/बहाल काम 1330 शायरी के होते हैं। या तो इस काम के लेखक का नाम ज्ञात नहीं है। अब तक, इसकी खोज पाया जानकारी के आधार पर एक व्यक्ति है जो ) परंपरा के लिए निकली लेखक हो सकता है। कि नाम में तिरुवल्लुवर [थिरू] के रूप में हुई")
        st.sidebar.table(side_table)
    else:
        st.error("Invalid language selection.")
        return pd.DataFrame()
    
     # User input for Thirukkural search
    

    # Search button
    if st.button("Search"):
        # Perform the search based on the selected language
        result = search_thirukkural(user_input, selected_language)
        

        # Display results or inform the user if no match is found
        try:
            if result['Fuzzy_Score'] < 10:
                st.warning("No matching Thirukkural found.")
            else:
                # Display individual content with border boxes
                #st.subheader("Thirukkural Details:")
                

                if selected_language == 'தமிழ்':
                    custom_string = ""
                    st.markdown(f"<div class='container-header center-text'>{'தமிழ்'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>அதிகாரம்:</span> {result['அதிகாரம்']}<br><span class='key'>இயல்:</span> {result['இயல்']}<br><span class='key'>பால்:</span> {result['பால்']}<br><span class='key'>தமிழ்:</span>{result['தமிழ்']}<br><span class='key'>தமிழ் விளக்கம்:</span> {result['Tamil_Explanation']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container-header center-text'>{'English'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>Chapter:</span> {result['Chapter']}<br><span class='key'>Book:</span> {result['Book']}<br><span class='key'>Division:</span> {result['Division']}<br><span class='key'>English:</span> {result['English']}<br><span class='key'>English Explanation:</span> {result['English_explanation']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container-header center-text'>{'हिन्दी'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>अध्याय:</span> {result['अध्याय-chapter']}<br><span class='key'>पुस्तक:</span> {result['पुस्तक-book']}<br><span class='key'>विभाजन:</span> {result['विभाजन-Division']}<br><span class='key'>हिन्दी:</span> {result['हिन्दी']}<br><span class='key'>विवरण:</span>{result['Hindi_Explanation']}</div>", unsafe_allow_html=True)
                
                elif selected_language == 'English':
                    st.markdown(f"<div class='container-header center-text'>{'English'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>Chapter:</span> {result['Chapter']}<br><span class='key'>Book:</span> {result['Book']}<br><span class='key'>Division:</span> {result['Division']}<br><span class='key'>English:</span> {result['English']}<br><span class='key'>English Explanation:</span> {result['English_explanation']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container-header center-text'>{'தமிழ்'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>அதிகாரம்:</span> {result['அதிகாரம்']}<br><span class='key'>இயல்:</span> {result['இயல்']}<br><span class='key'>பால்:</span> {result['பால்']}<br><span class='key'>தமிழ்:</span>{result['தமிழ்']}<br><span class='key'>தமிழ் விளக்கம்:</span> {result['Tamil_Explanation']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container-header center-text'>{'हिन्दी'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>अध्याय:</span> {result['अध्याय-chapter']}<br><span class='key'>पुस्तक:</span> {result['पुस्तक-book']}<br><span class='key'>विभाजन:</span> {result['विभाजन-Division']}<br><span class='key'>हिन्दी:</span> {result['हिन्दी']}<br><span class='key'>विवरण:</span>{result['Hindi_Explanation']}</div>", unsafe_allow_html=True)
                    
                elif selected_language == 'हिन्दी':
                    st.markdown(f"<div class='container-header center-text'>{'हिन्दी'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>अध्याय:</span> {result['अध्याय-chapter']}<br><span class='key'>पुस्तक:</span> {result['पुस्तक-book']}<br><span class='key'>विभाजन:</span> {result['विभाजन-Division']}<br><span class='key'>हिन्दी:</span> {result['हिन्दी']}<br><span class='key'>विवरण:</span>{result['Hindi_Explanation']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container-header center-text'>{'தமிழ்'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>அதிகாரம்:</span> {result['அதிகாரம்']}<br><span class='key'>இயல்:</span> {result['இயல்']}<br><span class='key'>பால்:</span> {result['பால்']}<br><span class='key'>தமிழ்:</span>{result['தமிழ்']}<br><span class='key'>தமிழ் விளக்கம்:</span> {result['Tamil_Explanation']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container-header center-text'>{'English'}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='container center-text content'><span class='key'>Chapter:</span> {result['Chapter']}<br><span class='key'>Book:</span> {result['Book']}<br><span class='key'>Division:</span> {result['Division']}<br><span class='key'>English:</span> {result['English']}<br><span class='key'>English Explanation:</span> {result['English_explanation']}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.warning("No matching Thirukkural found.")

if __name__ == "__main__":
    main()
