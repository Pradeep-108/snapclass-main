import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    # Card CSS
    st.markdown("""
    <style>

    /* Card */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border-radius: 35px !important;
        border: none !important;
        padding: 20px !important;
    }

    /* Card title */
    .portal-title {
        font-size: 30px;
        font-weight: 900;
        line-height: 0.9;
        color: #202020;
        margin-bottom: 10px;
    }

    /* Button */
    div.stButton > button {
        background: #f33ba0 !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important; 
        font-weight: 600 !important;
        padding: 8px 18px 
    }

    </style>
    """, unsafe_allow_html=True)


    # Two columns
    col1, col2 = st.columns(2, gap="large")


    # ================= STUDENT =================

    with col1:

        with st.container():

            st.markdown("""
            <div class="portal-title">
                I'm<br>
                Student
            </div>
            """, unsafe_allow_html=True)

            st.image(
                "src/images/Student.png",
                width=75
            )

            if st.button(
                "Student Portal ↗",
                key="student"
            ):
                st.session_state["login_type"] = "student"
                st.rerun()


    # ================= TEACHER =================

    with col2:

        with st.container():

            st.markdown("""
            <div class="portal-title">
                I'm<br>
                Teacher
            </div>
            """, unsafe_allow_html=True)

            st.image(
                "src/images/Teacher.png",
                width=100
            )

            if st.button(
                "Teacher Portal ↗",
                key="teacher"
            ):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    
    
    
    footer_home()