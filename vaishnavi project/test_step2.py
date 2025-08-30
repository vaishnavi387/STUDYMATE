from processor import extract_text_from_pdf, chunk_text

# Replace with path to your own PDF
pdf_path = "sample.pdf"

# Extract text
text = extract_text_from_pdf(pdf_path)
print("Extracted text (first 500 chars):")
print(text[:500])

# Chunk it
chunks = chunk_text(text)
print(f"\nTotal chunks created: {len(chunks)}")
print("First chunk:\n", chunks[0])
