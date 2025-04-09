from .chroma_cli import chromadb_client
from .llm import llm_gpt


def handler_query_v1(query=None, top_k=2):
    prompt_template = '''
      你是企业员工助手，熟悉公司考勤和报销标准等规章制度，需要根据提供的上下文信息context来回答员工的提问。\
      请直接回答问题，如果上下文信息context没有和问题相关的信息，请直接回答[不知道,请咨询HR] \
      问题：{question} 
      "{context}"
      回答：
      '''
    if not query:
        return "您有什么问题请直说"
    related_docs = chromadb_client.query(query, top_k)
    llm_prompt = prompt_template.replace("{question}", query).replace("{context}", related_docs)
    response = llm_gpt(llm_prompt, stream=False)
    print(f"response: ", response)
    return response, related_docs


if __name__ == "__main__":
    print(handler_query_v1("GraphRAG是什么?"), 2)
