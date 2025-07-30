import streamlit as st
from scripts.query_pipeline import query_medical_bot
import streamlit as st
from ocr.ocr_utils import extract_text_from_image
st.title("🩺 Medical QA Chatbot")

user_input = st.text_input("Ask a medical question:")
if user_input:
    answer = query_medical_bot(user_input)
    st.markdown(f"**Answer:** {answer}")

st.sidebar.title("📄 Upload Scan / Prescription")
uploaded_image = st.sidebar.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
    with open("temp_scan.png", "wb") as f:
        f.write(uploaded_image.read())
    
    extracted_text = extract_text_from_image("temp_scan.png")
    st.subheader("🧾 Extracted Text")
    st.text_area("OCR Result", extracted_text, height=150)

