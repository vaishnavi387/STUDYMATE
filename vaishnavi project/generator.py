import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load .env
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = os.getenv("HF_MODEL", "google/flan-t5-base")

# Initialize client
client = InferenceClient(model=HF_MODEL, token=HF_API_KEY)

def generate_answer(question, context):
    prompt = f"""You are StudyMate, an academic assistant.
Answer the question based ONLY on the context below.
If the answer is not found in the context, say "I could not find the answer in the provided material."

Context:
{context}

Question: {question}
Answer:"""

    response = client.text2text_generation(
        prompt=prompt,
        max_new_tokens=300
    )

    # Return the generated text
    return response["generated_text"]

