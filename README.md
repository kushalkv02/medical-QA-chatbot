# 🩺 Medical QA Chatbot (RAG-based)

A chatbot that answers medical questions using RAG over WHO documents and medical guides.

## Features
- Local embeddings with multilingual support
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
