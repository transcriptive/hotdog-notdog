import streamlit as st
import pickle

st.title('Hotdog-Notdog')
st.header('Is this a photo of a delicious assorted meat tube, or a photo of something else?')


#upload an image
image = st.file_uploader('Upload an image')

if image:
    st.text('Here is the image you just uploaded')
    st.image(image)