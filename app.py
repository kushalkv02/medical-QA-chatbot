import streamlit as st
from scripts.query_pipeline import query_medical_bot

st.title("🩺 Medical QA Chatbot")

user_input = st.text_input("Ask a medical question:")
if user_input:
    answer = query_medical_bot(user_input)
    st.markdown(f"**Answer:** {answer}")