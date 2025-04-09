import environs
import os

env = environs.Env()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env.read_env(os.path.join(BASE_DIR, '.env'))

llm_base_url = env.str('llm_base_url', "")
llm_api_key = env.str('llm_api_key', "")
chromadb_host = env.str('chromadb_host', "")
chromadb_port = env.int('chromadb_port', 8080)
device = env.str('device', "cpu")

if __name__ == "__main__":
    print(BASE_DIR+"/third_party/embeddings_models/bge-m3/")
    print(llm_base_url)
    print(llm_api_key)
