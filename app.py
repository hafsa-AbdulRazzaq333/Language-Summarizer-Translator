# cd "C:\Users\ALL AtoZ\Desktop\Main Projects\Language-Translator-main"
# venv\Scripts\activate
# streamlit run app.py

import os
import streamlit as st
from utils.controller import summarize_and_translate

# ——————————————————————————————————————————————————————————————————————————
# 1. Page Config & CSS
# ——————————————————————————————————————————————————————————————————————————
st.set_page_config(
    page_title="Language Summerizer and Translator",
    layout="centered",
    page_icon="🌐"
)

st.markdown("""
<style>
/* Page background */
body { background-color: #f0f2f6; }

/* Header */
h1 { text-align: center; color: #4f46e5; font-size: 2.5rem; margin-bottom: 0.1rem; }
.subtitle { text-align: center; color: #6b7280; font-size: 1.1rem; margin-bottom: 2rem; }

/* Card container */
.card {
  background: #ffffff;
  padding: 2rem;
  margin: 1rem auto;
  border-radius: 0.75rem;
  max-width: 700px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Text areas */
.css-1hynsf2 textarea {
  border-radius: 0.5rem !important;
}

/* Buttons */
.stButton>button {
  background-color: #6366f1 !important;
  color: #ffffff !important;
  border-radius: 0.5rem !important;
  padding: 0.6rem 1.2rem !important;
  font-size: 1rem !important;
  border: none !important;
}
.stButton>button:hover {
  background-color: #4f46e5 !important;
}
</style>
""", unsafe_allow_html=True)

# ——————————————————————————————————————————————————————————————————————————
# 2. Header
# ——————————————————————————————————————————————————————————————————————————
st.markdown("<h1>🌐 Language Translation App</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Summarize and translate any text using Groq’s AI</p>", unsafe_allow_html=True)

# ——————————————————————————————————————————————————————————————————————————
# 3. Translation Card
# ——————————————————————————————————————————————————————————————————————————
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Input form
    with st.form(key="translate_form"):
        sentence = st.text_area(
            "📝 Enter text to summarize and translate:",
            height=150,
            placeholder="Type or paste your text here..."
        )
        # Language selector
        languages = [
            "French", "Spanish", "German", "Chinese", "Japanese",
            "Russian", "Arabic", "Portuguese", "Hindi", "Urdu", "Other"
        ]
        target_language = st.selectbox("🌍 Target language:", languages)
        if target_language == "Other":
            target_language = st.text_input("Specify language:")
        
        submit = st.form_submit_button("Summarize & Translate ▶️")
    st.markdown("</div>", unsafe_allow_html=True)

# ——————————————————————————————————————————————————————————————————————————
# 4. Perform Summarize + Translation & Display
# ——————————————————————————————————————————————————————————————————————————
if submit:
    if sentence.strip() and target_language.strip():
        with st.spinner("Processing…"):
            summary, translation = summarize_and_translate(sentence, target_language)
        st.success("✅ Done!")

        # Show results in a second card
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🧾 Summary")
        st.text_area("Summary:", value=summary, height=120)

        st.subheader("🌐 Translation")
        st.text_area("Translated Text:", value=translation, height=150)

        st.download_button(
            "📥 Download Translation as TXT",
            data=translation,
            file_name="translation.txt",
            mime="text/plain",
            use_container_width=True
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter both the text and the target language.")
