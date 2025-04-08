from langchain_text_splitters import RecursiveCharacterTextSplitter

"""
文本分块函数
"""


def text_splitter(docs=None):
    if docs is None:
        docs = []

    doc_data = []
    doc_spliter = RecursiveCharacterTextSplitter(chunk_size=128,  # 单个文件块128长度
                                                 chunk_overlap=30,  # 允许重复内容为30长度

                                                 separators=["\n\n",
                                                             "\n",
                                                             ".",
                                                             "\uff0e",  # Fullwidth full stop
                                                             "\u3002",  # Ideographic full stop
                                                             ",",
                                                             "\uff0c",  # Fullwidth comma
                                                             "\u3001",  # Ideographic comma
                                                             ])
    for data in docs:
        content = data["content_with_weight"]
        if '<table>' not in content and len(content) > 200:
            doc_data = doc_data + doc_spliter.split_text(content)
        else:
            doc_data.append(content)
    return doc_data
