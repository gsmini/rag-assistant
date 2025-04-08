import environs
import os

env = environs.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(BASE_DIR, '.env'))

llm_base_url = env.str('llm_base_url')
llm_api_key = env.str('llm_api_key')
chromadb_host = env.str('chromadb_host')
chromadb_port = env.str('chromadb_port')
device = env.str('device')
