import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Choose Your Language",
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
    padding-top: 70px;
}

/* Title */

.language-title {
    text-align: center;
    color: #285943;
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* Description */

.language-description {
    text-align: center;
    color: #657269;
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 35px;
}

/* Radio text */

div[data-testid="stRadio"] label {
    font-size: 17px !important;
}

/* Continue button */

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
    '<div class="language-title">Choose Your Language</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="language-description">'
    'Select the language you are most comfortable speaking.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- LANGUAGE SELECTION ----------------

language = st.radio(
    "Choose a language:",
    [
        "தமிழ் — Tamil",
        "हिन्दी — Hindi",
        "മലയാളം — Malayalam",
        "తెలుగు — Telugu",
        "ಕನ್ನಡ — Kannada",
        "मराठी — Marathi",
        "ગુજરાતી — Gujarati",
        "English"
    ]
)


# ---------------- CONTINUE ----------------

if st.button("CONTINUE", use_container_width=True):

    if language == "தமிழ் — Tamil":
        st.switch_page("pages/create_account.py")

    else:
        st.warning(
            "This language is not available in our current prototype. "
            "Please select Tamil to continue."
        )