import chromadb
import numpy as np
from chromadb.utils import embedding_functions

from config import chromadb_host, chromadb_port
"""
向量数据库操作
"""
chroma_client = chromadb.HttpClient(host=chromadb_host, port=chromadb_port)

if __name__ == "__main__":
    model_path = '../embdding-demo/gte-large-zh/'
    em_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_path)
    collection = chroma_client.create_collection(name='rag_db',
                                                 embedding_function=em_fn,  # 指定embedding 函数
                                                 metadata={"hnsw:space": "cosine"})
    documents = ["在向量搜索领域，我们拥有多种索引方法和向量处理技术，\
        它们使我们能够在召回率、响应时间和内存使用之间做出权衡。",
                 "虽然单独使用特定技术如倒排文件（IVF）、乘积量化（PQ）\
                 或分层导航小世界（HNSW）通常能够带来满意的结果",
                 "GraphRAG 本质上就是 RAG，只不过与一般 RAG 相比，其检索路径上多了一个知识图谱"]
    collection.add(documents=documents,
                   ids=["id1", "id2", "id3"],
                   metadatas=[{"chapter": 3, "verse": 16},
                              {"chapter": 4, "verse": 5},
                              {"chapter": 12, "verse": 5}])

    print(collection.peek(limit=1))  # 获取第一条

    # 查询

    get_collection = chroma_client.get_collection(name='rag_db',
                                                  embedding_function=em_fn)
    id_result = get_collection.get(ids=['id2'],
                                   include=["documents", "embeddings_models", "metadatas"])

    print(np.array(id_result['embeddings_models']).shape)  # (1, 1024) 1条数据 1024纬度 和我们之前单独使用ebemdding模型的时候效果是一样的

    # 语意搜索
    query = '索引技术有哪些？'
    get_collection.query(query_texts=query,
                         n_results=2,  # 取前两个匹配到的结果
                         include=["documents", 'metadatas'])
    # 语意搜索 直接根据元数据过滤
    get_collection.query(query_texts=query,
                         n_results=2,
                         include=["documents", 'metadatas'],
                         where={"verse": 5})
    # 混合检索支持的操作
    """
    - $eq - equal to (string, int, float)
    
    - $ne - not equal to (string, int, float)
    
    - $gt - greater than (int, float)
    
    - $gte - greater than or equal to (int, float)
    
    - $lt - less than (int, float)
    
    - $lte - less than or equal to (int, float)
    """
    get_collection.query(
        query_texts=["索引技术有哪些？"],
        n_results=2,
        where={"chapter": {"$lt": 10}},  # 运算符的支持
    )
