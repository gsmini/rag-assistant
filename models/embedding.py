from config import device, BASE_DIR
# from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

"""
向量化文本
"""


class RagBgeM3Embedding:
    def __init__(self,
                 model_path=BASE_DIR + "/third_party/embeddings_models/bge-m3/",
                 device=device):
        encode_kwargs = {'normalize_embeddings': True}  # 标准归一化

        self.embedding = HuggingFaceEmbeddings(model_name=model_path,
                                               model_kwargs={"device": device},
                                               encode_kwargs=encode_kwargs
                                               )

    def get_embedding_fun(self):
        return self.embedding


bgem3_embedding = RagBgeM3Embedding()

if __name__ == "__main__":
    pass
