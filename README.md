# chromadb
```shell

docker run -d --name chromadb -p 8000:8000 \
-v ./chroma:/chroma/chroma \
-e IS_PERSISTENT=TRUE\
 -e ANONYMIZED_TELEMETRY=TRUE \
 chromadb/chroma:0.6.3
```
> https://cookbook.chromadb.dev/running/running-chroma/#docker
> pip install chromadb==0.6.3 客户端版本和docker启动的版本要对齐 不然无法执行相关业务


# python3.10.5
```shell
virtualenv -p ~/.pyenv/versions/3.10.5/bin/python rag-assistant-env
source  rag-assistant-env/bin/activate
pip install -r requirements.txt
```

# ragflow本地下载
```shell
cd third_party
git clone  https://github.com/infiniflow/ragflow.git
rm -rf .git

```
>  这里我已经下载了  可自行根据最新版本下载，然后修改import的路径
# embedding 模型下载
```shell

cd  third_patry/embeddings_models
git clone https://www.modelscope.cn/BAAI/bge-m3.git
```
## 本地依赖安装
```shell
pip install poetry
poetry install -E full
```
> 我想用ragflow中的文档解析功能，所以把源码下载下来安装依赖

## bug 修改

```shell
        finally:
            self.pdf.close()
```
> 删除 third_party/ragflow/deepdoc/parser/pdf_parser.py 1037行 这是bug?