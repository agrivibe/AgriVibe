import streamlit as st

st.title("AgriVibe-க்கு வரவேற்கிறோம்!")

st.write("உங்கள் விவசாயப் பிரச்சினைகளுக்கு எளிய மற்றும் விரைவான தீர்வுகளைப் பெறுங்கள்.")

if st.button("தொடங்கலாம்"):
    st.switch_page("pages/home.py")