import os
import streamlit as st

if "username" not in st.session_state:
    st.session_state["username"] = None


def login_frontend():
    existing_usernames = os.listdir("user_data")
    st.title("**Login / Sign Up**")
    username = st.text_input("Username")
    # Remove trailing and leading whitespace
    username = username.strip()
    if st.button("Submit"):
        st.session_state["username"] = username
        st.session_state["video_processing_stage"] = "upload_video"
        st.session_state["processed_video"] = None
        if st.session_state["username"] in existing_usernames:
            st.success("Welcome back!")
        else:
            st.warning("New user detected. A new folder will be created for you.")
            os.makedirs(f"user_data/{st.session_state['username']}")
