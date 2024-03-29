import streamlit as st
from PIL import Image
from video_processing.frontend import process_video_frontend

st.set_page_config(
    page_title="LectureGenie Home",
    layout="centered",
    page_icon=Image.open("icons/icon_icon.png"),
    initial_sidebar_state="expanded",
)
import add_title
add_title.add_logo()

if "video_processing_stage" not in st.session_state:
    st.session_state.video_processing_stage = None



col1, col2, col3 = st.columns(3)

col2.write(r"$\textsf{\Huge LectureGenie}$")


cols = st.columns(2)




st.write("##### Upload your lecture videos and get interactive quizzes, notes and flashcards")



st.markdown(
    """

    1. **Go to the sidebar** to login and/or upload a video
    2. Once the video has been processed you can:
        - **Go to Video Quiz** for an interactive quiz
        - **Go to Notes Generator** to get detailed notes
        - **Go to Flashcard Generator** to get flashcards
"""
)

with cols[1]:
    process_video_frontend()





st.warning("Uploaded videos are not secure, anyone who knows your username can access your videos."
           " Do not upload sensitive information. Videos will be deleted after 24 hours. This is only a prototype.")
st.warning("The things said and shown in the video are sent to a third party AI provider which may store the data for"
           " improving their own services.")


# Embed ko-fi
st.markdown(
   "[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/A0A5VDT0M)"
)