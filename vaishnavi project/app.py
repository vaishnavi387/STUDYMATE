import streamlit as st
import tempfile
from processor import extract_text_from_pdf, chunk_text
from embedder import build_faiss_index, search_index
from generator import generate_answer

st.set_page_config(page_title="StudyMate", page_icon="📘")
st.title("📘 StudyMate: AI-Powered PDF Q&A")

uploaded_files = st.file_uploader("Upload PDF(s)", type="pdf", accept_multiple_files=True)

if uploaded_files:
    all_chunks = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            text = extract_text_from_pdf(tmp.name)
            chunks = chunk_text(text)
            all_chunks.extend(chunks)

    index, _ = build_faiss_index(all_chunks)
    st.success("✅ Documents processed successfully!")

    query = st.text_input("Ask a question:")
    if query:
        retrieved = search_index(query, index, all_chunks)
        context = " ".join(retrieved)
        answer = generate_answer(query, context)

        st.markdown("### 📖 Answer")
        st.write(answer)

        st.markdown("### 📚 References")
        for i, chunk in enumerate(retrieved, 1):
            st.markdown(f"**{i}.** {chunk[:300]}...")
