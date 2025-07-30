# 🩺 Medical QA Chatbot (RAG-based)

A chatbot that answers medical questions using RAG over WHO documents and medical guides.

## Features
- Fast vector search using Chroma
- Local LLM inference using Mistral (no API costs!)
- Streamlit frontend

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
