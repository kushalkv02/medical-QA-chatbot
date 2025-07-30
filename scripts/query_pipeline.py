# scripts/query_pipeline.py

from llama_cpp import Llama
import chromadb
import textwrap

# Load Phi-2 model (Q4_K_M) from your local models folder
llm = Llama(
    model_path="models/phi-2.Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=4,
    n_gpu_layers=30  # For M1 GPU acceleration, adjust as needed
)

# Connect to Chroma vector store
chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_or_create_collection(name="medical")

def format_prompt(query, docs):
    context = "\n\n".join([f"Source {i+1}: {textwrap.shorten(doc, width=500)}" for i, doc in enumerate(docs)])
    return f"""### Context:
{context}

### Question:
{query}

### Answer:"""

def query_medical_bot(query, top_k=3):
    # Step 1: Embed query and retrieve top chunks
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    documents = [doc for doc in results['documents'][0]]

    # Step 2: Build prompt
    prompt = format_prompt(query, documents)

    # Step 3: Generate answer
    output = llm(prompt, max_tokens=512, stop=["\n\n", "###"])
    answer = output["choices"][0]["text"].strip()
    return answer
