import uuid

import chromadb

from config import chromadb_host, chromadb_port

from models.embedding import bgem3_embedding
from langchain_core.documents import Document
from langchain_chroma import Chroma

"""
向量数据库操作
用langchain_chroma实现的 所以和直接用chromadb使用方式还有点小区别
"""


class Chromadb:
    def __init__(self):
        self.chroma_client = chromadb.HttpClient(host=chromadb_host, port=chromadb_port)
        self.dbname = "rag-assistant"
        self.db_metadata = {"hnsw:space": "cosine"}  # 相似度为余弦相似度计算规则
        self.embedding_model_beg_m3 = bgem3_embedding
        # self.get_or_create_collect(self.dbname)
        self.vector_store = Chroma(
            collection_name=self.dbname,
            embedding_function=self.embedding_model_beg_m3.get_embedding_fun(),
            client=self.chroma_client,
        )

    # 创建collection
    def get_or_create_collect(self, collect_name):
        collection = self.chroma_client.get_or_create_collection(name=collect_name,
                                                                 embedding_function=self.embedding_model_beg_m3.get_embedding_fun(),
                                                                 metadata=self.db_metadata
                                                                 )

        return collection

    # 删除collection
    def del_collection(self, name):
        self.chroma_client.delete_collection(name)

    def add_doc(self, docs):
        langchain_docs = []
        doc_ids = []
        for idx, chunk in enumerate(docs):
            is_table = 0
            if "table" in chunk:
                is_table = 1
            if idx == len(docs) - 1:
                is_table = 1
            doc_id = str(uuid.uuid4())
            document = Document(
                page_content=chunk,
                metadata={"type": "ori", "is_table": is_table})
            langchain_docs.append(document)
            doc_ids.append(doc_id)


        self.vector_store .add_documents(langchain_docs)
        return doc_ids

    def delete_doc(self, doc_id):
        self.vector_store .delete(doc_id)

    def query(self, query_texts, top_k):

        # 语意搜索
        related_docs = self.vector_store.similarity_search(query_texts, top_k)
        print(related_docs)
        for doc in related_docs:
            print(doc)
        context = "\n".join([f"上下文{i + 1}: {doc.page_content} \n" for i, doc in enumerate(related_docs)])
        return context


chromadb_client = Chromadb()

if __name__ == "__main__":
    # 创建
    documents = [
        "在向量搜索领域，我们拥有多种索引方法和向量处理技术，它们使我们能够在召回率、响应时间和内存使用之间做出权衡。",
        "虽然单独使用特定技术如倒排文件（IVF）、乘积量化（PQ）或分层导航小世界（HNSW）通常能够带来满意的结果",
        "GraphRAG 本质上就是 RAG，只不过与一般 RAG 相比，其检索路径上多了一个知识图谱"
    ]

    ids = chromadb_client.add_doc(documents)

    # 查询
    query = 'GraphRAG 本质是什么'
    print(chromadb_client.query(query, 2))





# # 混合检索支持的操作
# """
# - $eq - equal to (string, int, float)
#
# - $ne - not equal to (string, int, float)
#
# - $gt - greater than (int, float)
#
# - $gte - greater than or equal to (int, float)
#
# - $lt - less than (int, float)
#
# - $lte - less than or equal to (int, float)
# """
# get_collection.query(
#     query_texts=["索引技术有哪些？"],
#     n_results=2,
#     where={"chapter": {"$lt": 10}},  # 运算符的支持
# )
