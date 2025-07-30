# 🩺 Medical QA Chatbot (RAG-based)

A chatbot that answers medical questions using RAG over WHO documents and medical guides.

## Features
- Fast vector search using Chroma
- Local LLM inference using Mistral (no API costs!)
- Streamlit frontend
- Optional OCR for scanned reports

## Setup
1. Place PDFs in `data/raw/`
2. Run `extract_text.py` → `embed_chunks.py`
3. Launch app with `streamlit run app.py`

## Credits
- Mistral from Hugging Face (quantized)
- Sentence-Transformers multilingual models
- WHO publications (public domain)
- Phi2 model developers

##Example prompts
1. what is anti microbial resistance
2. what is Maintenance Therapy
3. what is Rapid Endovenous Therapy
4. what is Oral Rehydration Therapy
5. what is Medical Devices Regulation
6. what is a vaccine

Note: Currently works on limited prompts over Phi2 model. We can extend the functionalitty by using models with greater parameters like mistral.

example result:
<img width="1439" height="528" alt="Screenshot 2025-07-30 at 6 34 35 PM" src="https://github.com/user-attachments/assets/b7aca4a4-788f-4587-ba21-f3af78f3ed0e" />
<img width="1439" height="821" alt="Screenshot 2025-07-30 at 6 36 28 PM" src="https://github.com/user-attachments/assets/158e10f4-800f-4362-9026-8ed4b78d1a59" />

