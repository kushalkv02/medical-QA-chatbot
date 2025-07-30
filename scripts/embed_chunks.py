from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
import uuid
import os

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

chroma_client = chromadb.Client(chromadb.config.Settings(
    persist_directory="chroma_store"
))
collection = chroma_client.get_or_create_collection("medical")

for file in os.listdir("data"):
    if file.endswith(".txt"):
        with open(f"data/{file}", "r") as f:
            text = f.read()
        chunks = text_splitter.split_text(text)
        embeddings = model.encode(chunks).tolist()

        # Generate unique IDs for each chunk
        ids = [str(uuid.uuid4()) for _ in range(len(chunks))]

        collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=[{"source": file}] * len(chunks),
            ids=ids
        )
        print(f"✅ Embedded {len(chunks)} chunks from {file}")