from abc import ABC

from langchain.llms.base import LLM
from openai import OpenAI
from config import llm_api_key, llm_base_url
from typing import Any, List, Optional

mode_name = "gpt-4o"


class ChatGptLLM(LLM, ABC):
    client: Optional[Any] = None

    def __init__(self):
        super().__init__()
        self.client = OpenAI(base_url=llm_base_url,
                             api_key=llm_api_key)

    def _call(self,
              prompt,
              stop=None,
              run_manager=None,
              **kwargs):
        print(prompt)
        completion = self.client.chat.completions.create(model=mode_name,
                                                         messages=[
                                                             {
                                                                 "role": "user",
                                                                 "content": prompt
                                                             }
                                                         ])
        return completion.choices[0].message.content

    @property
    def _llm_type(self) -> str:
        return mode_name


llm_gpt = ChatGptLLM()
if __name__ == "__main__":
    prompt_template = '''
    你是企业员工助手，熟悉公司考勤和报销标准等规章制度，需要根据提供的上下文信息context来回答员工的提问。\
    请直接回答问题，如果上下文信息context没有和问题相关的信息，请直接回答[不知道,请咨询HR] \
    问题：{question} 
    "{context}"
    回答：
    '''

    """
    # 案例1 直接问大模型
    query = "GraphRAG 本质是什么？"

    context = "在向量搜索领域，我们拥有多种索引方法和向量处理技术，它们使我们能够在召回率、响应时间和内存使用之间做出权衡。"
    llm_prompt = prompt_template.replace("{question}", query).replace("{context}", context)
    response = llm_gpt(llm_prompt, stream=False)
    print(f"response: ", response)
    # for chunk in response:
    #     print(chunk.choices[0].text, end='', flush=True)
    
        """

    # 案例2 rag+大模型
    """
    """
    from chroma_cli import chromadb_client

    query = 'GraphRAG 本质是什么？'
    related_docs = chromadb_client.query(query, 2)
    llm_prompt = prompt_template.replace("{question}", query).replace("{context}", related_docs)
    response = llm_gpt(llm_prompt, stream=False)
    print(f"response: ", response)
