import fitz  # PyMuPDF

def extract_text_from_pdf(path):
    """Extract all text from a PDF file"""
    text = ""
    with fitz.open(path) as doc:
        for page_num, page in enumerate(doc, start=1):
            text += f"\n[Page {page_num}]\n"
            text += page.get_text("text")
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks"""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks
