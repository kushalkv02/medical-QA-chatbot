import fitz  # PyMuPDF
import os

def extract_text_from_pdfs(pdf_folder="data/raw"):
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            print(f"📄 Found PDF: {file}")
            doc = fitz.open(os.path.join(pdf_folder, file))
            full_text = "\n".join([page.get_text() for page in doc])
            out_path = f"data/{file[:-4]}.txt"
            with open(out_path, "w") as f:
                f.write(full_text)
            print(f"✅ Extracted to {out_path}")
        else:
            print(f"⏩ Skipped non-PDF: {file}")

# Call the function
extract_text_from_pdfs()
