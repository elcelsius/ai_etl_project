# AI Copilot - Serviço de ETL e RAG

Este projeto implementa um pipeline completo de **Retrieval-Augmented Generation (RAG)**, projetado para servir como o núcleo de um copiloto de IA para um sistema web complexo.

O objetivo é ler, processar e indexar uma base de conhecimento privada (documentação, código-fonte, diagramas) e fornecer uma interface de consulta inteligente, capaz de responder perguntas complexas sobre o projeto de forma precisa e sem alucinações, utilizando a API do Google Gemini.

---

## 📋 Principais Funcionalidades

* **Pipeline de ETL Modular:** Processa múltiplos formatos de arquivo (`.pdf`, `.docx`, `.txt`, `.md`, e arquivos de código como `.php`, `.sql`).
* **Base de Conhecimento Vetorial:** Utiliza o `sentence-transformers` para gerar embeddings de alta qualidade e o `FAISS` para criar um índice vetorial de busca rápida.
* **Aceleração por GPU:** O processo de geração de embeddings e a busca são acelerados utilizando a GPU via CUDA, garantindo alta performance.
* **Persistência de Metadados:** Armazena os chunks de texto e metadados em um banco de dados **PostgreSQL** para referência e consistência.
* **Geração de Respostas com LLM:** Integra-se com a API do **Google Gemini** para sintetizar respostas coesas e precisas a partir do contexto recuperado.
* **Ambiente Containerizado:** Todo o serviço roda em **Docker** e **Docker Compose**, garantindo portabilidade e facilidade de configuração.

---

## 🛠️ Stack de Tecnologias

* **Linguagem:** Python 3.11
* **Orquestração:** Docker & Docker Compose
* **IA & Machine Learning:**
    * LangChain
    * Sentence Transformers (`all-MiniLM-L6-v2`)
    * FAISS-GPU
    * PyTorch
    * Google Generative AI (Gemini 1.5 Flash)
* **Banco de Dados:** PostgreSQL 15
* **Ambiente Base:** Imagem NVIDIA CUDA no Ubuntu 22.04

---

## 🚀 Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o projeto.

### Pré-requisitos

* Git
* Docker Desktop
* WSL2 (para usuários Windows)
* Drivers NVIDIA com suporte a CUDA para WSL instalados no host.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/elcelsius/ai_etl_project.git](https://github.com/elcelsius/ai_etl_project.git)
    cd ai_etl_project
    ```

2.  **Configure as variáveis de ambiente:**
    Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`.
    ```bash
    cp .env.example .env
    ```
    Agora, **edite o arquivo `.env`** e preencha com suas credenciais, especialmente sua `GOOGLE_API_KEY`.

3.  **Popule a base de conhecimento:**
    Adicione seus arquivos de documentação, código-fonte e outros materiais na pasta `data/`. O ETL irá escanear todas as subpastas recursivamente.

4.  **Construa a imagem Docker:**
    Este comando irá baixar a imagem base da NVIDIA e instalar todas as dependências. Pode demorar na primeira vez.
    ```bash
    docker-compose build
    ```

---

## 💡 Como Usar

### 1. Executando o Pipeline de ETL

Para processar os arquivos da pasta `data/` e (re)criar a base de conhecimento:
```bash
docker-compose run --rm etl python3 etl_orchestrator.py