import streamlit as st
import os
from PIL import Image

stage = "home"

if "stage" not in st.session_state:
    st.session_state.stage = "home"

st.title("Imagify")

st.write(" ")
st.write(" ")
st.write(" ")

   

   

files  = st.file_uploader("Select Image", type=["jpg","png","jpeg"])

def home():

    if files is not None:

       imgae = Image.open(files)
       st.write(" ")
       st.write(" ")
       st.write(" ")

       st.image(imgae, caption="hehehehe", width=300)

    st.write(" ")
    st.write(" ")
    if st.button("Try Grayscale", type="primary"):
        st.session_state.stage = "grayscale"

    st.write(" ")
    st.write(" ")

    if st.button("Resize Your Image", type="primary"):
        st.session_state.stage = "resize"


def grayscaler():
    st.write(" ")
    st.write(" ")
    st.subheader("Grayscale Your Image ")

    image = Image.open(files)

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("Grayscale Inage ", type="primary"):
        g_image = image.convert('L')

        st.write(" ")
        st.write(" ")
        st.write(" ")

        st.image(g_image, caption="Grayscale Image", width=300)

        st.write(" ")
        st.write (" ")

        if st.button("Return To Home", type="primary"):
            st.session_state.stage = "home"
        



def resize():
    st.write(" ")
    st.write(" ")
    st.subheader("Resize Your Image")

    width = st.number_input("width")
    height = st.number_input("height")

    st.write(" ")
    st.write(" ")

    image = Image.open(files)
    
    if st.button("Resize"):
        r_image = image.resize((width,height))

        st.image(r_image, caption="Resized Image", width=300)

        st.write(" ")
        st.write(" ")
         
        if st.button("Return to Home"):
            st.session_state.stage = "home" 


            
def rotate():
    pass


    

if st.session_state.stage == "home":
    home()

elif st.session_state.stage == "grayscale":
    grayscaler()

elif st.session_state == "resize":
    resize()
