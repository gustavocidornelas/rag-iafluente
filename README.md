# RAG `iafluente`

Esse repositório acompanha o tutorial [Introdução a RAG]() do `iafluente`.

Você pode utilizar esse repositório para acompanhar o tutorial ou como ponto de partida para a sua própria aplicação de RAG.

> A estrutura do repositório é uma réplica desse template, disponibilizado pelo Openlayer.

## Como executar

### Indexação

Primeiro, é importante criar o banco de dados de vetores para o RAG. Isso é feito no notebook [`notebooks/indexing.ipynb`](/notebooks/index.ipynb). Execute o notebook para criar o  banco de vetores.

### Aplicação

Com o banco de vetores criado, é possível executar a aplicação. Para isso:

1. Instale as dependências e adicione a sua API key da OpenAI no arquivo `.env`:

```bash
pip install -r requirements.txt
cp .env.example .env # Crie o arquivo .env. Depois, adicione a sua API key da OpenAI
```

2. Execute a aplicação, que deve ser disponibilizada no `localhost:5000`.

```bash
python app/server.py
```

Navegue para o `localhost:5000` e faça perguntas sobre tutoriais do `iafluente`.

Essa aplicação é utiliza RAG por trás das cenas e a pipeline RAG é definida no arquivo [`app/model/rag.py`](/app/model/rag.py).

