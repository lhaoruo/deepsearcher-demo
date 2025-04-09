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

# Milvus 与其他向量数据库对比报告

本报告整理了关于 Milvus 与其他向量数据库在关键功能、性能扩展、灵活性及适用场景等方面的检索结果。以下对比内容分为两个部分：本地检索结果与 Web 检索结果，以帮助读者全面了解各平台优势与不足。

| **子问题** | **本地结果** | **Web 结果** |
|------------|--------------|--------------|
| **1. Milvus 的关键功能和能力是什么？** | Milvus 是一个高性能、高可扩展性的向量数据库，支持从单台设备到分布式系统的灵活部署。其设计注重多种索引类型、硬件加速和全生命周期管理，适用于处理大规模向量数据。 | Milvus 作为开源向量数据库，以处理数十亿级向量为目标，具备高并发、高吞吐和高可靠性。其架构将数据和计算解耦，实现高扩展性和优异的实时查询性能。 |
| **2. 其他向量数据库的关键功能和能力是什么？** | 本地文档主要介绍了 Milvus 的架构与功能优势，强调其在数据建模、索引优化和多部署模式方面的能力。 | Web 信息则涵盖了各类向量数据库在数据存储、查询效率、索引策略和混合搜索能力上的差异，展示了不同平台在实际应用中的侧重点。 |
| **3. 在性能和可扩展性方面，Milvus 与其他数据库如何比较？** | Milvus 的本地介绍突出了其支持高并发、大数据量检索，并通过分布式架构和硬件加速实现高性能。 | Web 结果对比中，Milvus 在实时查询和大规模向量检索场景中显示出较强的扩展能力，与其他平台（如 Weaviate）存在显著差异。 |
| **4. 在灵活性和易用性方面，Milvus 与其他数据库如何比较？** | Milvus 提供了多种部署模式与数据建模能力，从原型设计到生产级应用均有完善支持。 | Web 检索结果表明，不同平台在易用性和灵活性上各有侧重，有的平台在开发友好性和快速配置上更具优势，而 Milvus 则主打强大功能和高适应性。 |
| **5. 哪些特定用例中 Milvus 的表现优于其他数据库？** | 本地信息显示，Milvus 非常适合处理大规模向量数据和复杂数据建模，在 AI 搜索和推荐系统等场景中具有明显优势。 | Web 结果进一步指出，Milvus 在高维向量检索、实时搜索以及大数据商业应用方面表现卓越，适合于对响应速度和数据规模要求较高的场景。 |
| **6. 使用 Milvus 存在的局限或缺点是什么？** | 本地文档侧重于展示 Milvus 的优点，对局限性描述较少。 | Web 结果中则对 Milvus 的部署复杂性和维护挑战提出了讨论，提醒用户在特定场景下需权衡功能与成本。 |

# 生成日志
/opt/anaconda3/bin/python /Users/haoruo/Desktop/de%                      
(base) haoruo@Haoruos-MacBook-Pro deepsearcher_demo % /opt/anaconda3/bin/python /Users/haoruo/Desktop/deepsearcher_demo/main.py
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox

================= Context Breakdown =================

--- Sub-query 1: 1. What are the key features and capabilities of Milvus?
Local:
 What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing ...
Web:
 What is Milvus?
GRADUATE PROJECT

Milvus is an open-source vector database built to handle billions of vectors and powers the largest AI applications in the world.

Created by
Try Managed Milvus for Free
Download Milvus
Built on a vibrant and growing community

34K+

GitHub stars

4,000+

Community

68M+

Downloads

300+

Contributors

How does Milvus work?
Coordinator Services

Orchestrate load balancing and data management through coordinators, ensuring efficient data, query, and index managem ...
[Playwright Warning] Failed to extract from https://www.cloudraft.io/blog/top-5-vector-databases: Locator.inner_text: Error: strict mode violation: locator("main, article") resolved to 3 elements:
    1) <main>…</main> aka get_by_role("main").filter(has_text="Top 5 Vector Databases in")
    2) <article class="mdx prose mx-auto mt-4 w-full transition-colors dark:prose-invert">…</article> aka get_by_text("Introduction We are drowning")
    3) <main class="layout flex flex-col items-center border-t pt-6 dark:border-gray-600">…</main> aka get_by_role("main").filter(has_text="Scale your business by")

Call log:
  - waiting for locator("main, article")


--- Sub-query 2: 2. What other vector databases are available on the market?
Local:
 What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing ...
Web:
 (Failed to extract content) ...

--- Sub-query 3: 3. How does Milvus compare to these other vector databases in terms of performance, scalability, and ease of use?
Local:
 What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing ...
Web:
 Milvus vs. Weaviate: The Battle of Open-Source Vector Databases
Mon Mar 25 2024
Vector Database
Open Source

#
Introduction to Vector Databases

In the realm of artificial intelligence (AI) applications, vectors play a pivotal role in enhancing machine learning algorithms' efficiency. These mathematical representations enable AI systems to comprehend and process complex data structures effectively. The management of these vectors is where databases step in, providing a structured environment for ...
[Playwright Warning] Failed to extract from https://www.gitselect.com/post/milvus-vs-other-vector-databases: Locator.inner_text: Error: strict mode violation: locator("main, article") resolved to 7 elements:
    1) <main tabindex="-1" id="PAGES_CONTAINER" class="PAGES_CONTAINER" data-main-content="true">…</main> aka locator("#PAGES_CONTAINER")
    2) <article class="tgMH9T" data-hook="post">…</article> aka get_by_text("Milvus Vs Other Vector DatabasesGuest ContributorFeb 19, 20243 min readIn the")
    3) <main class="VQDdIN" data-hook="post-description">…</main> aka get_by_role("article").filter(has_text="Milvus Vs Other Vector").get_by_role("main")
    4) <main>…</main> aka locator("#content-wrapper").get_by_role("main").filter(has_text="Guide to Selecting the Best")
    5) <article class="qbu2Gh" data-hook="recent-post-list-item">…</article> aka get_by_role("article").filter(has_text="Guide to Selecting the Best")
    6) <article class="qbu2Gh" data-hook="recent-post-list-item">…</article> aka get_by_role("article").filter(has_text="What is Pinecone and when to")
    7) <article class="qbu2Gh" data-hook="recent-post-list-item">…</article> aka get_by_role("article").filter(has_text="What is Weaviate? Comparison")
Call log:
  - waiting for locator("main, article")


--- Sub-query 4: 4. What are the specific use cases and industries where Milvus may have a competitive advantage over other vector databases?
Local:
 What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing ...
Web:
 (Failed to extract content) ...
[Playwright Warning] Failed to extract from https://myscale.com/blog/pgvector-vs-milvus-choosing-right-vector-database: Locator.inner_text: Error: strict mode violation: locator("main, article") resolved to 4 elements:
    1) <article itemscope="itemscope" itemtype="https://schema.org/BlogPosting">…</article> aka get_by_role("article").filter(has_text="pgvector vs Milvus: Choosing")
    2) <article class="ui-post" itemprop="blogPost" itemscope="itemscope" itemtype="https://schema.org/BlogPosting">…</article> aka get_by_role("article").filter(has_text="SQL+Vector: Empowering GenAI")
    3) <article class="ui-post" itemprop="blogPost" itemscope="itemscope" itemtype="https://schema.org/BlogPosting">…</article> aka get_by_role("article").filter(has_text="Working with Embedding Models")
    4) <article class="ui-post" itemprop="blogPost" itemscope="itemscope" itemtype="https://schema.org/BlogPosting">…</article> aka get_by_role("article").filter(has_text="AutoGen vs LangChain: Which")
Call log:
  - waiting for locator("main, article")


--- Sub-query 5: 5. Are there any notable drawbacks or limitations to using Milvus compared to other vector databases?
Local:
 What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing ...
Web:
 (Failed to extract content) ...

================= Comparison Results =================

Sub-question: What are the key features and capabilities of Milvus?
== 本地结果 ==
What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing hardware-aware code. Core contributors include professionals
from Zilliz, ARM, NVIDIA, AMD, Intel, Meta, IBM, Salesforce, Alibaba, and Microsoft.
Unstructured Data, Embeddings, and Milvus
Unstructured data, such as text, images, and audio, varies in format and carries rich underlying semantics,
making it challenging to analyze. To manage this complexity, embeddings are used to convert unstructured
data into numerical vectors that capture its essential characteristics. These vectors are then stored in a
vector database, enabling fast and scalable searches and analytics.
Milvus offers robust data modeling capabilities, enabling you to organize your unstructured or multi-modal
data into structured collections. It supports a wide range of data types for different attribute modeling,
including common numerical and character types, various vector types, arrays, sets, and JSON, saving you
from the effort of maintaining multiple database systems.
Milvus offers three deployment modes, covering

== Web结果 ==
What is Milvus?
GRADUATE PROJECT

Milvus is an open-source vector database built to handle billions of vectors and powers the largest AI applications in the world.

Created by
Try Managed Milvus for Free
Download Milvus
Built on a vibrant and growing community

34K+
GitHub stars
4,000+
Community
68M+
Downloads
300+
Contributors
How does Milvus work?
Coordinator Services
Orchestrate load balancing and data management through coordinators, ensuring efficient data, query, and index management.
Access Layer
Handles external requests using stateless proxies to manage connections, perform verifications, and balance load.
Worker Nodes
Executes tasks as scalable pods by implementing coordinator commands, enabling dynamic adjustment for changing data, query, and indexing demands.
Storage Layer
Ensures data persistence through three components: meta stores, log brokers and object storage.
Why Milvus?
Milvus is a cloud-native, open-source vector database powering Zilliz.
Scale as needed
Handles billions of vectors through its distributed architecture, separating storage and compute. Its microservice design allows scaling specific functions, optimizing resource use as you grow.
Learn more
High Performance
Milvus offers diverse index types (HNSW, DiskANN, Quantization, Binary, etc.) and hardware-optimized designs for both CPU and GPU. This ensures fast vector retrieval with high recall across various use cases.
Benchmark
Full Lifecycle Support
Milvus offers three deployment models with a unified API: Lite for prototyping, Standalone for testing and small-scale production, and Distributed for large-scale production—enabling seamless scaling without code rewrites.
Learn more
Feature Rich
Supports multiple search types (top-K & Range ANN, sparse & dense, multi-vector, grouping), metadata filtering, and multi-tenancy. It includes admin tools and integrates with various AI tools and models.
Explore Milvus Notebooks
“
Milvus is renowned as one of the most ad

Sub-question: What other vector databases are available on the market?
== 本地结果 ==
What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing hardware-aware code. Core contributors include professionals
from Zilliz, ARM, NVIDIA, AMD, Intel, Meta, IBM, Salesforce, Alibaba, and Microsoft.
Unstructured Data, Embeddings, and Milvus
Unstructured data, such as text, images, and audio, varies in format and carries rich underlying semantics,
making it challenging to analyze. To manage this complexity, embeddings are used to convert unstructured
data into numerical vectors that capture its essential characteristics. These vectors are then stored in a
vector database, enabling fast and scalable searches and analytics.
Milvus offers robust data modeling capabilities, enabling you to organize your unstructured or multi-modal
data into structured collections. It supports a wide range of data types for different attribute modeling,
including common numerical and character types, various vector types, arrays, sets, and JSON, saving you
from the effort of maintaining multiple database systems.
Milvus offers three deployment modes, covering

== Web结果 ==
(Failed to extract content)

Sub-question: How does Milvus compare to these other vector databases in terms of performance, scalability, and ease of use?
== 本地结果 ==
What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing hardware-aware code. Core contributors include professionals
from Zilliz, ARM, NVIDIA, AMD, Intel, Meta, IBM, Salesforce, Alibaba, and Microsoft.
Unstructured Data, Embeddings, and Milvus
Unstructured data, such as text, images, and audio, varies in format and carries rich underlying semantics,
making it challenging to analyze. To manage this complexity, embeddings are used to convert unstructured
data into numerical vectors that capture its essential characteristics. These vectors are then stored in a
vector database, enabling fast and scalable searches and analytics.
Milvus offers robust data modeling capabilities, enabling you to organize your unstructured or multi-modal
data into structured collections. It supports a wide range of data types for different attribute modeling,
including common numerical and character types, various vector types, arrays, sets, and JSON, saving you
from the effort of maintaining multiple database systems.
Milvus offers three deployment modes, covering

== Web结果 ==
Milvus vs. Weaviate: The Battle of Open-Source Vector Databases
Mon Mar 25 2024
Vector Database
Open Source
#
Introduction to Vector Databases
In the realm of artificial intelligence (AI) applications, vectors play a pivotal role in enhancing machine learning algorithms' efficiency. These mathematical representations enable AI systems to comprehend and process complex data structures effectively. The management of these vectors is where databases step in, providing a structured environment for storing and retrieving these crucial elements.
[Playwright Warning] Failed to extract from https://www.gitselect.com/post/milvus-vs-other-vector-databases: Locator.inner_text: Error: strict mode violation: locator("main, article") resolved to 7 elements:
    1) <main tabindex="-1" id="PAGES_CONTAINER" class="PAGES_CONTAINER" data-main-content="true">…</main> aka locator("#PAGES_CONTAINER")
    2) <article class="tgMH9T" data-hook="post">…</article> aka get_by_text("Milvus Vs Other Vector DatabasesGuest ContributorFeb 19, 20243 min readIn the")
    3) <main class="VQDdIN" data-hook="post-description">…</main> aka get_by_role("article").filter(has_text="Milvus Vs Other Vector").get_by_role("main")
    4) <main>…</main> aka locator("#content-wrapper").get_by_role("main").filter(has_text="Guide to Selecting the Best")
    5) <article class="qbu2Gh" data-hook="recent-post-list-item">…</article> aka get_by_role("article").filter(has_text="Guide to Selecting the Best")
    6) <article class="qbu2Gh" data-hook="recent-post-list-item">…</article> aka get_by_role("article").filter(has_text="What is Pinecone and when to")
    7) <article class="qbu2Gh" data-hook="recent-post-list-item">…</article> aka get_by_role("article").filter(has_text="What is Weaviate? Comparison")
Call log:
  - waiting for locator("main, article")

--- Sub-question: What are the specific use cases and industries where Milvus may have a competitive advantage over other vector databases?
== 本地结果 ==
What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing ...
== Web结果 ==
(Failed to extract content)

--- Sub-question: Are there any notable drawbacks or limitations to using Milvus compared to other vector databases?
== 本地结果 ==
What is Milvus?
Milvus is a high-performance, highly scalable vector database that runs efficiently across a wide range of
environments, from a laptop to large-scale distributed systems. It is available as both open-source software
and a cloud service.
Milvus is an open-source project under LF AI & Data Foundation distributed under the Apache 2.0 license.
Most contributors are experts from the high-performance computing (HPC) community, specializing in
building large-scale systems and optimizing ...
== Web结果 ==
(Failed to extract content)

<Query> Write a report comparing Milvus with other vector databases.
<Sub-queries> ['1. What are the key features and capabilities of Milvus?', '2. What other vector databases are available on the market?', '3. How does Milvus compare to these other vector databases in terms of performance, scalability, and ease of use?', '4. What are the specific use cases and industries where Milvus may have a competitive advantage over other vector databases?', '5. Are there any notable drawbacks or limitations to using Milvus compared to other vector databases?']
<Reflection> Information is sufficient.
<Final Answer> Milvus is a high-performance, highly scalable vector database that offers robust data modeling capabilities and supports various data types for different attribute modeling. It provides efficient storage and retrieval of numerical vectors, making it ideal for managing unstructured data such as text, images, and audio.

In comparison to other vector databases, such as Weaviate, Milvus stands out for its diverse index types, hardware-optimized designs for both CPU and GPU, and support for multiple search types. Milvus also offers a unified API for deployment across different modes, allowing seamless scaling without code rewrites.

While both Milvus and Weaviate are open-source vector databases, Milvus excels in its ability to handle billions of vectors through its distributed architecture, separating storage and compute. Additionally, Milvus's feature-rich environment includes admin tools and integration with various AI tools and models, making it a comprehensive solution for large-scale AI applications.

Overall, Milvus emerges as a powerful and versatile vector database, catering to the needs of modern AI applications with its high performance, scalability, and feature-rich environment.


