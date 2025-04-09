# deepsearcher-demo

手动实现deepsearcher核心逻辑：
向量构建 + 语义检索 + 大模型问答

## 使用方式

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=你的API_KEY
python main.py
```
# Milvus 与其他向量数据库对比报告

本报告基于本地和 Web 检索结果对 Milvus 与其他向量数据库在功能、性能、灵活性、使用场景及局限性等方面进行对比。

## 对比结果

| **子问题** | **本地结果** | **Web 结果** |
|------------|--------------|--------------|
| **1. Milvus 的关键功能和能力是什么？** | What is Milvus? <br> Milvus 是一个高性能、高扩展性的向量数据库，支持从笔记本到分布式系统的部署，开源并提供云服务。<br>（后续部分省略…） | What is Milvus? <br> GRADUATE PROJECT <br> Milvus 是一个开源向量数据库，支持处理数十亿级别向量... <br> （后续部分省略…） |
| **2. 其他向量数据库的关键功能和能力是什么？** | What is Milvus? <br> （与 Milvus 相关的本地介绍，主要关注架构和功能优势） | What is Cloud Computing? ... <br> 后续展示了关于向量数据库如何存储、查询和处理数据的说明<br> （后续部分省略…） |
| **3. 在性能和可扩展性方面，Milvus 与其他数据库有何比较？** | What is Milvus? <br> （详细介绍了 Milvus 的高性能、硬件加速等特性） | Milvus vs. Weaviate: The Battle of Open-Source Vector Databases <br> 简述了 Milvus 在扩展性和性能方面的优势<br> （后续部分省略…） |
| **4. 在灵活性和易用性方面，Milvus 与其他数据库有何比较？** | What is Milvus? <br> （同上，主要涉及数据建模和部署模式） | Vector Database Comparison <br> 提供了 Milvus 与其他数据库（如 Weaviate、Qdrant 等）的直观比较<br> （后续部分省略…） |
| **5. 哪些特定的用例中 Milvus 的表现优于其他数据库？** | What is Milvus? <br> （侧重于 Milvus 在大规模数据场景下的优势） | Discover more from Ankur’s Newsletter <br> 描述了 Milvus 在特定场景下（例如 AI 搜索、向量检索）如何突出优势<br> （后续部分省略…） |
| **6. 使用 Milvus 存在哪些局限或缺点？** | What is Milvus? <br> （同上，列出 Milvus 的部分局限性） | Blog: Choosing a Vector Database: Milvus vs. Chroma DB <br> 对比分析中提到了 Milvus 在某些场景下的不足<br> （后续部分省略…） |

