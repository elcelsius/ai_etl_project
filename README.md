# 🤖 AI Copilot -- Servico de ETL e RAG Generico

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![NVIDIA](https://img.shields.io/badge/NVIDIA-CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

Este projeto implementa um pipeline completo de Retrieval-Augmented
Generation (RAG), projetado para servir como o nucleo de um copiloto de
IA para qualquer sistema web complexo.

Ele le, processa e indexa uma base de conhecimento privada
(documentacao, codigo-fonte, diagramas) e fornece uma interface de
consulta inteligente.

## 📊 Diagrama do Fluxo do Sistema

``` mermaid
graph TD
    U[Usuario] --> H[Pergunta do usuario]

    A[Pasta de documentos doc, pdf, txt, xls] --> B[ETL Inicio]
    B --> C[Extracao de arquivos]
    C --> D[Transformacao dos dados]
    D --> E[Geracao de embeddings transforma texto em vetor]
    E --> F[Indexacao vetorial]
    E --> G[Banco de dados com metadados]
    F --> J[Busca vetorial]
    H --> I[Conversao da pergunta em vetor]
    I --> J
    J --> K[Recuperar trechos relevantes]
    G --> K
    K --> L[Montar prompt com contexto]
    L --> M[Modelo de linguagem]
    M --> N[Resposta para o usuario]
    N --> U
```

## 📋 Principais Funcionalidades

-   Pipeline de ETL modular
-   Base de conhecimento vetorial com FAISS
-   Geracao de embeddings com sentence-transformers
-   Persistencia em PostgreSQL
-   Integracao com Google Gemini
-   Execucao via Docker Compose

## 🚀 Como Configurar

``` bash
git clone https://github.com/elcelsius/ai_etl_project.git
cd ai_etl_project
cp .env.example .env
docker-compose build
chmod +x *.sh
```

## 🧠 Uso

Treinar:

``` bash
./treinar_ia.sh
```

Iniciar chat:

``` bash
./iniciar_chat.sh
```

## ⚙️ Observacoes

-   Para CPU: substituir faiss-gpu por faiss-cpu
-   Remover configuracao de GPU no docker-compose

------------------------------------------------------------------------

Desenvolvido por **Celso Lisboa**
