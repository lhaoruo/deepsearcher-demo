# main.py
# 复刻 deepsearcher 逻辑：向量构建 + 语义召回 + 大模型回答

import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from openai import OpenAI
import pdfplumber

# 设置 OpenAI API Key
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  
)
# 加载文档内容（这里只从 sample_data 文件夹读取所有 pdf 文件）
def load_documents(folder="./sample_data"):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            with pdfplumber.open(os.path.join(folder, filename)) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                docs.append(text)
    return docs

documents = load_documents()
print(f"已加载 {len(documents)} 篇文档")

# 构建文本向量索引
model = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = model.encode(documents)
dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

# 用户输入问题，转换成向量，进行检索
query = "Write a report about Milvus."
query_vec = model.encode([query])
D, I = index.search(np.array(query_vec), k=2)
retrieved_docs = [documents[i] for i in I[0]]
context = "\n".join(retrieved_docs)


prompt = f"""Please write a short report about Milvus based on the following information:

{context}
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# 用户输入问题
print("<Query>", query)
# 检索最相关文档
print("<Search>", retrieved_docs)
# 思考（构造prompt）
print("<Think>", prompt)
# 最终回答
print("<Respond>", response.choices[0].message.content)

