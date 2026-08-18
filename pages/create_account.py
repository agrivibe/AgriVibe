import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Create Account - AgriVibe",
    page_icon="🌱",
    layout="centered"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background-color: white;
}

.block-container {
    max-width: 480px;
    padding-top: 60px;
    padding-bottom: 40px;
}

/* Heading */
.signup-title {
    text-align: center;
    color: #285943;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 5px;
}

/* Subtitle */
.signup-subtitle {
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

</style>
""", unsafe_allow_html=True)


# ---------------- HEADING ----------------

st.markdown(
    '<div class="signup-title">Create Your Account</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="signup-subtitle">'
    'Join AgriVibe and get help for your crops 🌱'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- NAME ----------------

name = st.text_input(
    "Your Name",
    placeholder="Enter your name"
)


# ---------------- PHONE NUMBER ----------------

st.markdown(
    '<p style="color:#285943; font-weight:600; margin-bottom:5px;">'
    'Phone Number'
    '</p>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 4])

with col1:
    st.text_input(
        "Country Code",
        value="+91",
        disabled=True,
        label_visibility="collapsed"
    )

with col2:
    phone = st.text_input(
        "Mobile Number",
        placeholder="Enter 10-digit number",
        max_chars=10,
        label_visibility="collapsed"
    )


# ---------------- PASSWORD ----------------

password = st.text_input(
    "Create Password",
    placeholder="Enter your password",
    type="password"
)


# ---------------- CONFIRM PASSWORD ----------------

confirm_password = st.text_input(
    "Confirm Password",
    placeholder="Re-enter your password",
    type="password"
)


# ---------------- CREATE ACCOUNT ----------------

if st.button("CREATE ACCOUNT", use_container_width=True):

    # Check name
    if not name:
        st.warning("Please enter your name.")

    # Check phone
    elif not phone:
        st.warning("Please enter your phone number.")

    elif not phone.isdigit():
        st.error("Phone number must contain numbers only.")

    elif len(phone) != 10:
        st.error("Please enter exactly 10 digits.")

    # Check password
    elif not password:
        st.warning("Please create a password.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    # Everything is correct
    else:
        st.session_state["account_created"] = True


# ---------------- SUCCESS ----------------

if st.session_state.get("account_created", False):

    st.success("Your account has been created successfully! 🎉")

    if st.button("CONTINUE", use_container_width=True):
        st.switch_page("pages/welcome.py")