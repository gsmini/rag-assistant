from langchain_text_splitters import RecursiveCharacterTextSplitter

"""
文本分块函数
@content: 输入的待分块文本
@return: 返回分块后的文本列表
"""


def text_splitter(content=None):
    if content is None:
        content = ""

    split_data = []
    spliter = RecursiveCharacterTextSplitter(chunk_size=128,  # 单个文件块128长度
                                             chunk_overlap=30,  # 允许重复内容为30长度

                                             separators=["\n\n",
                                                         "\n",
                                                         ".",
                                                         "\uff0e",  # 中文句号。
                                                         "\u3002",  # 中文句号。
                                                         ",",
                                                         "\uff0c",  # 中文，
                                                         "\u3001",  # 中文、
                                                         ])
    if '<table>' not in content and len(content) > 200:
        split_data = split_data + spliter.split_text(content)
    else:
        split_data.append(content)
    return split_data


if __name__ == "__main__":
    pass
