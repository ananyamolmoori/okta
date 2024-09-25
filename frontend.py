import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OIDC Configuration
OIDC_CLIENT_ID = os.getenv("OIDC_CLIENT_ID")
OIDC_ISSUER = os.getenv("OIDC_ISSUER")
OIDC_REDIRECT_URI = os.getenv("OIDC_REDIRECT_URI")

# Streamlit title
st.title("Name Input Form")

# OIDC Login Flow
if 'access_token' not in st.session_state:
    st.write("Please log in to proceed.")
    if st.button("Login"):
        # Redirect to Okta login page
        auth_url = f"{OIDC_ISSUER}/v1/authorize?client_id={OIDC_CLIENT_ID}&response_type=token&redirect_uri={OIDC_REDIRECT_URI}&scope=openid profile email"
        #st.experimental_set_query_params()
        st.markdown(f'<a href="{auth_url}" target="_self">Click here to log in</a>', unsafe_allow_html=True)
else:
    name = st.text_input("Enter your name:")

    if st.button("Submit"):
        if name:
            response = requests.post("http://127.0.0.1:8000/submit-name/", json={"name": name}, headers={
                "Authorization": f"Bearer {st.session_state.access_token}"
            })
            if response.status_code == 200:
                message = response.json().get("message")
                st.success(message)
            else:
                st.error("Failed to submit name.")
        else:
            st.warning("Please enter your name.")

