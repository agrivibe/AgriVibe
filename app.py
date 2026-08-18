import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AgriVibe",
    page_icon="🌱",
    layout="centered"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background-color: white;
}

/* Main page spacing */
.block-container {
    max-width: 480px;
    padding-top: 70px;
    padding-bottom: 40px;
}

/* Welcome text */
.welcome {
    text-align: center;
    color: #285943;
    font-size: 28px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #6B756E;
    font-size: 15px;
    margin-bottom: 30px;
}

/* Input labels */
label {
    color: #285943 !important;
    font-weight: 600 !important;
}

/* Input boxes */
div[data-baseweb="input"] {
    border-radius: 12px;
    border: 1px solid #D7DED4;
    background-color: white;
}

div[data-baseweb="input"]:focus-within {
    border-color: #4E8B57;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 45px;
    font-weight: 600;
    font-size: 15px;
    border: none;
    background-color: #4E8B57;
    color: white;
}

div.stButton > button:hover {
    background-color: #3F7548;
    color: white;
}

/* Forgot password */
.forgot {
    text-align: center;
    color: #4E8B57;
    font-size: 14px;
    margin: 12px 0 18px 0;
}

</style>
""", unsafe_allow_html=True)


# ---------------- CENTERED LOGO ----------------

# Empty space above logo makes it sit
# slightly lower and more central on the page

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        "Agrivibe .JPG",
        width=220
    )


# ---------------- WELCOME ----------------

st.markdown(
    '<div class="welcome">Welcome Back!</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI farm companion 🌱</div>',
    unsafe_allow_html=True
)


# ---------------- LOGIN FIELDS ----------------

username = st.text_input(
    "Username",
    placeholder="Enter your username"
)

password = st.text_input(
    "Password",
    placeholder="Enter your password",
    type="password"
)


# ---------------- LOGIN BUTTON ----------------

if st.button("LOG IN", use_container_width=True):

    if username and password:
        st.success("Login successful!")
        st.switch_page("pages/choose_language.py")

    else:
        st.warning("Please enter your username and password.")


# ---------------- FORGOT PASSWORD ----------------

st.markdown(
    '<div class="forgot">Forgot password?</div>',
    unsafe_allow_html=True
)


# ---------------- CREATE ACCOUNT ----------------

if st.button("CREATE AN ACCOUNT", use_container_width=True):
    st.switch_page("pages/choose_language.py")


