import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AgriVibe - Video Recorded",
    page_icon="🌱",
    layout="centered"
)

# ---------------- DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background-color: white;
}

.block-container {
    max-width: 650px;
    padding-top: 65px;
    padding-bottom: 50px;
}

/* Main title */

.main-title {
    text-align: center;
    color: #285943;
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 30px;
}

/* Success heading */

.success-title {
    text-align: center;
    color: #285943;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 15px;
}

/* Description */

.description {
    text-align: center;
    color: #657269;
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 38px;
}

/* What happens next */

.next-title {
    color: #285943;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* Steps */

.step {
    color: #657269;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 13px;
}

/* Analyze button */

div.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 13px;
    border: none;
    background-color: #4E8B57;
    color: white;
    font-size: 16px;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #3F7548;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">🌱 AgriVibe</div>',
    unsafe_allow_html=True
)


# ---------------- SUCCESS MESSAGE ----------------

st.markdown(
    '<div class="success-title">'
    '📹 Video Recorded Successfully!'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">'
    'Your crop video has been recorded successfully.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- WHAT HAPPENS NEXT ----------------

st.markdown(
    '<div class="next-title">What happens next?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="step">'
    '🔍 AgriVibe will analyze your crop video.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="step">'
    '🌱 Identify possible crop diseases or pests.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="step">'
    '💡 Suggest possible solutions.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="step">'
    '🎥 Provide step-by-step guidance.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- ANALYZE BUTTON ----------------

st.write("")

if st.button(
    "🔍 Analyze My Crop",
    use_container_width=True
):
    st.info("AI crop analysis is coming next!")