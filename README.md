# chromadb
```shell

docker run -d --name chromadb -p 8000:8000 \
-v ./chroma:/chroma/chroma \
-e IS_PERSISTENT=TRUE\
 -e ANONYMIZED_TELEMETRY=TRUE \
 chromadb/chroma:0.6.3
```
> https://cookbook.chromadb.dev/running/running-chroma/#docker


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
# embedding 模型下载
```shell

cd  third_patry
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