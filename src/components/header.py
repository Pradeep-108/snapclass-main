import streamlit as st
import base64


def header_home():

    with open("src/images/logo.png", "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px;">
            <img 
                src="data:image/png;base64,{encoded_image}" 
                style="height:100px;"
            />
            <h1 style='text-align:center; color:#E0E3FF;'>Snap Class</h1>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>Snap<br/>Class</h2>
        </div>   
                
                """, unsafe_allow_html=True)