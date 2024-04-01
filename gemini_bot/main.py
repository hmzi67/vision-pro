from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()   # Load all env variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# to load gemini pro vision
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type" : uploaded_file.type,   # getting mime type of uploaded file
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file found")
    


# initilize our streamlit app

st.set_page_config(page_title="ML Invoice Extractor")

st.header("Gemini App")
input = st.text_input("Input prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image.", use_column_width=True)

submit = st.button("Tell me about image")

input_prompt="""
You are an expert in understanding invoices. I'll upload an image as an invoice an then you have to answer
any question based on the uploaded invoice image
"""

# if submit is clicked 
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)