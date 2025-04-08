import warnings

from langchain.llms.base import LLM
from openai import OpenAI

warnings.filterwarnings('ignore')


class RagLLM:
    client = None

    def __init__(self):
        super().__init__()
        self.client = OpenAI(base_url="http://localhost:11434/v1/",
                             api_key="qwen2:72b")

    def __call__(self, prompt: str, **kwargs):
        completion = self.client.completions.create(model="qwen2:72b",
                                                    prompt=prompt,
                                                    temperature=kwargs.get('temperature', 0.1),
                                                    top_p=kwargs.get('top_p', 0.9),
                                                    max_tokens=kwargs.get('max_tokens', 4096),
                                                    stream=kwargs.get('stream', False))
        if kwargs.get('stream', False):
            return completion
        return completion.choices[0].text


class QwenLLM(LLM):
    client = None

    def __init__(self):
        super().__init__()
        self.client = OpenAI(base_url="http://localhost:11434/v1/",
                             api_key="qwen2:72b")

    def _call(self,
              prompt,
              stop=None,
              run_manager=None,
              **kwargs):
        completion = self.client.completions.create(model="qwen2:72b",
                                                    prompt=prompt,
                                                    temperature=kwargs.get('temperature', 0.1),
                                                    top_p=kwargs.get('top_p', 0.9),
                                                    max_tokens=kwargs.get('max_tokens', 4096),
                                                    stream=kwargs.get('stream', False))
        return completion.choices[0].text

    @property
    def _llm_type(self) -> str:
        return "rag_llm_qwen2_72b"
