# main.py
# Simplified DeepSearcher logic: sub-query decomposition + OpenAI embedding + OpenAI GPT response 

import os
import pdfplumber
from openai import OpenAI
import numpy as np

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load PDF documents from a single folder
def load_documents(folder):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder, filename)
            with pdfplumber.open(file_path) as pdf:
                text = ""
                for page in pdf.pages:
                    if page.extract_text():
                        text += page.extract_text()
                if text.strip():
                    docs.append(text)
    return docs

# Embed text using OpenAI Embedding API
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

# Compute cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    v1, v2 = np.array(vec1), np.array(vec2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Load documents
folder = "./sample_data"
documents = load_documents(folder)

# Get embeddings for each document
embedded_docs = [(doc, get_embedding(doc)) for doc in documents]

# User query
query = "Write a report comparing Milvus with other vector databases."

# Sub-query decomposition
sub_query_prompt = f"Please split the following question into sub-questions: {query}"
sub_resp = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": sub_query_prompt}]
)
sub_queries = sub_resp.choices[0].message.content.strip().split("\n")

# For each sub-query, find top-matching document using OpenAI embedding similarity
retrieved_texts = []
for sub_q in sub_queries:
    q_vec = get_embedding(sub_q)
    similarities = [(doc, cosine_similarity(q_vec, vec)) for doc, vec in embedded_docs]
    sorted_docs = sorted(similarities, key=lambda x: x[1], reverse=True)
    retrieved_texts.append(sorted_docs[0][0])  # Top-1 result

context = "\n".join(retrieved_texts)

# Reflection step
reflection_prompt = f"Based on the following context for the question '{query}', is there any missing information? If yes, suggest follow-up questions. If no, say 'Information is sufficient.'\n\nContext:\n{context}"
reflection_resp = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": reflection_prompt}]
)
reflection = reflection_resp.choices[0].message.content

# Final answer
final_prompt = f"Please write a report answering the question: {query}\n\nContext:\n{context}"
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": final_prompt}]
)

print("<Query>", query)
print("<Sub-queries>", sub_queries)
print("<Context>", context[:500], "...")
print("<Reflection>", reflection)
print("<Final Answer>", response.choices[0].message.content)

