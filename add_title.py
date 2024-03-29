import streamlit as st


def add_logo():
    if "processed_video" not in st.session_state:
        st.session_state["processed_video"] = None
    # The image is stored at icon.png

    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url("https://raw.githubusercontent.com/LectureGenieDevTeam/LectureGenie/main/icons/icon.png");
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 40px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Lecture Genie";
                margin-left: 20px;
                margin-top: 40px;
                font-size: 30px;
                position: absolute;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


add_logo()
