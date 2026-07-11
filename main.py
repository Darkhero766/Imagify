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


def grayscaler():
    st.write(" ")
    st.subheader("Grayscale Your Image ")

    image = Image.open(files)

    if st.button("Grayscale Inage ", type="secondary"):
        g_image = image.convert('L')

        st.write(" ")
        st.write(" ")
        st.write(" ")
        



def resize():
    st.write(" ")
    st.subheader("Resize Your Image")


    

if st.session_state.stage == "home":
    home()

elif st.session_state.stage == "grayscale":
    grayscaler()

elif st.session_state == "resize":
    resize()
