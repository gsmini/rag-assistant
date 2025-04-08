from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from config import device

"""
向量化文本
"""


class RagEmbedding:
    def __init__(self, model_path="third_party/embeddings_models/bge-m3/",
                 device=device):
        self.embedding = HuggingFaceEmbeddings(model_name=model_path,
                                               model_kwargs={"device": device})

    def get_embedding_fun(self):
        return self.embedding


if __name__ == "__mian__":
    pass
