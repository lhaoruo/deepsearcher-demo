import os
import pdfplumber
from openai import OpenAI
import numpy as np
import requests
from dotenv import load_dotenv

# 加载环境变量（确保 .env 文件中正确配置了 EXA_API_KEY 和 OPENAI_API_KEY）
load_dotenv()
EXA_API_KEY = os.getenv("EXA_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_documents(folder):
    """
    读取指定文件夹下的所有 PDF 文件，并将其中的文本内容合并后返回列表
    """
    docs = []
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            with pdfplumber.open(os.path.join(folder, file)) as pdf:
                text = ''.join(page.extract_text() or '' for page in pdf.pages)
                if text.strip():
                    docs.append(text)
    return docs

def get_embedding(text):
    """
    调用 OpenAI 接口获取文本的嵌入向量
    """
    return client.embeddings.create(model="text-embedding-ada-002", input=text).data[0].embedding

def cosine_similarity(vec1, vec2):
    """
    计算两个向量的余弦相似度
    """
    v1, v2 = np.array(vec1), np.array(vec2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def search_exa(query, top_k=1):
    """
    调用 Exa API 进行 Web 搜索，并返回格式化后的结果字符串列表
    """
    print("Loaded EXA_API_KEY:", EXA_API_KEY)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EXA_API_KEY}"
    }
    
    # 根据 Exa API 要求将 payload 放在顶层，字段包括：query, numResults, text
    payload = {
        "query": query,
        "numResults": top_k,
        "text": "true"   # 若 API 要求布尔值，可修改为 True
    }
    
    print("Headers:", headers)
    print("Payload:", payload)
    
    res = requests.post("https://api.exa.ai/search", json=payload, headers=headers)
    print("Response:", res.text)
    res.raise_for_status()
    
    results = res.json().get("results", [])
    formatted_results = []
    
    # 依次提取每个结果的标题、URL 以及 autopromptString（若有）
    for r in results:
        title = r.get("title", "(No title)")
        url = r.get("url", "(No URL)")
        autoprompt = r.get("autopromptString", "")
        formatted_results.append(f"Title: {title}\nURL: {url}\nAutoprompt: {autoprompt}")
        
    return formatted_results

def process_query(query, documents, top_k_web=1):
    """
    对输入的问题进行处理：
      1. 通过 OpenAI 将问题拆分为多个子问题；
      2. 对每个子问题分别从本地文档和 Web 搜索中获取结果，并进行对比；
      3. 将所有结果合并后作为上下文传递给 OpenAI 得到最终回答。
    """
    # 预先计算本地文档嵌入（如果文档较多，建议提前缓存）
    embedded_docs = [(doc, get_embedding(doc)) for doc in documents]
    
    # 拆分子问题
    subq_prompt = f"Split the question into sub-questions:\n{query}"
    subq = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": subq_prompt}])
    sub_queries = subq.choices[0].message.content.strip().split("\n")
    
    full_context = ""
    comparison_results = {}  # 用于存放每个子问题对应的本地和 Web 结果，便于对比
    
    print("\n================= Context Breakdown =================")
    for i, sq in enumerate(sub_queries):
        # 去掉前缀（如 "1. "）
        q_clean = sq.strip("1234567890. ")
        q_emb = get_embedding(q_clean)
        
        # 本地检索：计算每个文档与子问题的余弦相似度，取最相关的文本片段（截取前 1500 字符）
        local_docs_sorted = sorted(
            [(doc, cosine_similarity(q_emb, vec)) for doc, vec in embedded_docs],
            key=lambda x: x[1],
            reverse=True
        )
        local_text = local_docs_sorted[0][0][:1500] if local_docs_sorted else "(No local result)"
        
        # Web 检索：调用 Exa API
        web_results = search_exa(q_clean, top_k=top_k_web)
        web_text = "\n".join(web_results)
        
        # 保存本地与 Web 检索结果到对比字典中
        comparison_results[q_clean] = {"local": local_text, "web": web_text}
        
        # 打印每个子问题的对比结果
        print(f"\n--- Sub-query {i+1}: {sq.strip()}")
        print("Local:\n", local_text[:500], "...")
        print("Web:\n", web_text[:500], "...")
        
        full_context += f"[Local]\n{local_text}\n[Web]\n{web_text}\n"
    
    print("\n================= Comparison Results =================")
    for sub_q, results in comparison_results.items():
        print(f"\nSub-question: {sub_q}")
        print("== 本地结果 ==")
        print(results["local"])
        print("\n== Web结果 ==")
        print(results["web"])
    
    # 用 OpenAI 进行反思判断：基于上下文信息是否有缺失
    reflection_prompt = (
        f"Based on the following context for the question '{query}', "
        "is anything missing? If not, say 'Information is sufficient.'\n\nContext:\n" + full_context
    )
    reflection_resp = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": reflection_prompt}]
    )
    reflection = reflection_resp.choices[0].message.content
    
    # 最终回答：使用完整上下文生成最终答案
    final_prompt = (
        f"Please answer this question:\n'{query}'\n\nUse the following context:\n" + full_context
    )
    answer = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": final_prompt}]
    )
    
    print("\n<Query>", query)
    print("<Sub-queries>", sub_queries)
    print("<Reflection>", reflection)
    print("<Final Answer>", answer.choices[0].message.content)
    
    # 可选：返回对比结果以便后续进一步分析
    return comparison_results

if __name__ == "__main__":
    docs = load_documents("./sample_data")
    q = "Write a report comparing Milvus with other vector databases."
    process_query(q, docs, top_k_web=1)
