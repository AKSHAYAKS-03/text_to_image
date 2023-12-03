import requests
import streamlit as st
import io
from PIL import Image
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}
st.title("test to image Generator")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

prompt = st.text_input("enter your prompt")
button_prompt = st.button("generate img")
if button_prompt:
    image_bytes = query({
	    "inputs": prompt,
    })
# You can access the image with PIL.Image for example
    images = Image.open(io.BytesIO(image_bytes))
    st.image(images)