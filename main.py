import streamlit as st
import os
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from io import BytesIO

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

    if st.button("Compress The Image", type="primary"):
        st.session_state.stage = "compress"
    if st.button("Try Grayscale", type="primary"):
        st.session_state.stage = "grayscale"

    st.write(" ")

    if st.button("Resize Your Image", type="primary"):
        st.session_state.stage = "resize"

    st.write(" ")

    if st.button("Rotate Image", type="primary"):
        st.session_state.stage  = "rotate"

    st.write(" ")

    if st.button("Invert Colours", type="primary"):
        st.session_state.stage = "invert"

    st.write(" ")

    if st.button("Blur Image", type="primary"):
        st.session_state.stage = "blur"
    st.write(" ")

    if st.button("Change Brighttness", type="primary"):
        st.session_state.stage = "bright"
    
    st.write(" ")
    if st.button("Contrast Image", type="primary"):
        st.session_state.stage = "contrast"
    


def compress():
    st.write(" ")
    st.write(" ")

    st.header("Compress Image")
    st.write(" ")

    image = Image.open(files)

    original = len(files.getvalue()) / 1024

    st.write(f"original size : {original:.2f} KB")

    quality = st.slider("Select Quality", min_value=10, max_value=90, step=10)

    if st.button("Compress", type="primary"):
        st.write(" ")

        new = BytesIO()

        image  = image.convert("RGB")

        image.save(new, format="JPEG", quality=quality)

        new_size = len(new.getvalue()) / 1024

        st.write(f"Now Size : {new_size:.2f} KB")

        st.image(image, "compressed", width=500 )

        st.download_button(label="Download Compress Imge", data = new, file_name="compress.jpg", mime="image/jpeg")


    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button("Return To Home", type="secondary"):
        st.session_state.stage = "home"

        




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

    width = int(st.number_input("width"))
    height = int(st.number_input("height"))

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
    st.write(" ")
    st.write(" ")
    
    st.subheader("Rotate Image")

    image = Image.open(files)

    st.write(" ")

    st.write(" ")

    angle = st.sidebar.slider("Rotate Image", min_value=0)

    rotate_image = image.rotate(angle)

    if st.button("Rotate",type="primary" ):
        st.write(" ")
        st.image(rotate_image, caption="Rotated Image ",width=300)


    st.write(" ")
    if st.button("Return To Home", type="secondary"):
        st.session_state.stage = "home"


    
def invert():
    st.write(" ")
    st.write(" ")
    st.subheader("Invert Image Colors")

    image = Image.open(files)

    st.write(" ")
    st.write(" ")

    rgb = image.convert('RGB')

    if st.button("Invert colours", type="primary"):
        invert_img = ImageOps.invert(rgb)

        st.image(invert_img, caption="Inverted Image", width=500 )

        st.write(" ")
        st.write(" ")

    if st.button("Return To Home"):
        st.session_state.stage = "home"

def blur():
    st.write(" ")
    st.write(" ")

    st.subheader("blur Your image")
    st.write(" ")
    st.write(" ")

    image = Image.open(files)
    st.write(" ")

    if st.button("Blur Image"):
        b_image = image.filter(ImageFilter.BLUR)
        st.write(" ")

        st.image(b_image, caption="Blurr Image", width=500)

    st.write(" ")
    if st.button("Return To home"):
        st.session_state.stage = "home"

    
def bright():
    st.write(" ")

    st.header("Increase the brightness")
    st.write(" ")

    image = Image.open(files)

    brighty = st.slider("Increase brightness", min_value=0.0, max_value=5.0, step=0.1)

    enhncer = ImageEnhance.Brightness(image)
    
    if st.button("Increase Brightness"):

       b_image = enhncer.enhance(brighty)

       st.image(b_image, caption="Brightened Image", width=500)

    st.write(" ")
    st.write(" ")

    if st.button("Return home"):
        st.session_state.stage = "home"


def contrast():
    st.write(" ")

    st.header("Change The contrast")

    image = Image.open(files)
    st.write(" ")

    contrastt = st.slider("Increasethe contrast ", min_value=0.0, max_value=5.0, step=0.1)

    enhancer = ImageEnhance.Contrast(image)

    c_image = enhancer.enhance(contrastt)

    if st.button("Change Contrast"):
        st.image(c_image, caption="Contrasted Image", width=500)

    st.write(" ")

    if st.button("Return Home"):
        st.session_state.stage = "home"


if st.session_state.stage == "home":
    home()

elif st.session_state.stage == "grayscale":
    grayscaler()

elif st.session_state.stage == "resize":
    resize()

elif st.session_state.stage == "rotate":
    rotate()

elif st.session_state.stage == "invert":
    invert()

elif st.session_state.stage == "blur":
    blur()

elif st.session_state.stage == "bright":
    bright()

elif st.session_state.stage == "contrast":
    contrast()
elif st.session_state.stage == "compress":
    compress()
