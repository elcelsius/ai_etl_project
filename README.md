# AI Copilot - Serviço de ETL e RAG Genérico

[cite_start]Este projeto implementa um pipeline completo de **Retrieval-Augmented Generation (RAG)**, projetado para servir como o núcleo de um copiloto de IA para qualquer sistema web complexo. [cite: 1]

[cite_start]O objetivo é ler, processar e indexar uma base de conhecimento privada (documentação, código-fonte, diagramas) e fornecer uma interface de consulta inteligente, capaz de responder perguntas complexas sobre o projeto de forma precisa e sem alucinações, utilizando a API do Google Gemini. [cite: 1]

---

## 📋 Principais Funcionalidades

* [cite_start]**Pipeline de ETL Modular:** Processa múltiplos formatos de arquivo (`.pdf`, `.docx`, `.txt`, `.md`, e arquivos de código como `.php`, `.sql`). [cite: 1]
* [cite_start]**Base de Conhecimento Vetorial:** Utiliza `sentence-transformers` para gerar embeddings de alta qualidade e o `FAISS` para criar um índice vetorial de busca rápida. [cite: 1]
* [cite_start]**Aceleração por GPU:** O processo de geração de embeddings e a busca são acelerados utilizando a GPU via CUDA, garantindo alta performance. [cite: 1]
* [cite_start]**Persistência de Metadados:** Armazena os chunks de texto e metadados em um banco de dados **PostgreSQL** para referência e consistência. [cite: 1]
* [cite_start]**Geração de Respostas com LLM:** Integra-se com a API do **Google Gemini** para sintetizar respostas coesas e precisas a partir do contexto recuperado. [cite: 1]
* [cite_start]**Ambiente Containerizado:** Todo o serviço roda em **Docker** e **Docker Compose**, garantindo portabilidade e facilidade de configuração. [cite: 1]

---

## 🛠️ Stack de Tecnologias

* [cite_start]**Linguagem:** Python 3.11 [cite: 1]
* [cite_start]**Orquestração:** Docker & Docker Compose [cite: 1]
* **IA & Machine Learning:**
    * [cite_start]LangChain [cite: 1]
    * [cite_start]Sentence Transformers (`all-MiniLM-L6-v2`) [cite: 1]
    * [cite_start]FAISS-GPU [cite: 1]
    * [cite_start]PyTorch [cite: 1]
    * [cite_start]Google Generative AI (Gemini 1.5 Flash) [cite: 1]
* [cite_start]**Banco de Dados:** PostgreSQL 15 [cite: 1]
* [cite_start]**Ambiente Base:** Imagem NVIDIA CUDA no Ubuntu 22.04 [cite: 1]

---

## 🚀 Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o projeto em uma nova máquina.

### Pré-requisitos

* [cite_start]Git [cite: 1]
* [cite_start]Docker Desktop [cite: 1]
* [cite_start]WSL2 (para usuários Windows) [cite: 1]
* [cite_start]Drivers NVIDIA com suporte a CUDA para WSL instalados no host. [cite: 1]

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
    Agora, **edite o arquivo `.env`** e preencha com suas credenciais, especialmente sua `GOOGLE_API_KEY`. O conteúdo do `.env.example` deve ser:
    ```ini
    # Credenciais do Banco de Dados PostgreSQL
    POSTGRES_DB=ai_project
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432

    # Chave de API para o Google Gemini
    # Obtenha sua chave em: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
    GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
    ```

3.  **Popule a base de conhecimento:**
    Adicione os arquivos de documentação e código-fonte do seu projeto na pasta `data/`. [cite_start]O ETL irá escanear todas as subpastas recursivamente. [cite: 1]

4.  **Construa a imagem Docker:**
    Este comando irá baixar a imagem base da NVIDIA e instalar todas as dependências. Pode demorar na primeira vez.
    ```bash
    docker-compose build
    ```

5.  **Torne os scripts executáveis:**
    Este passo dá a permissão necessária para rodar os atalhos de treinamento e chat.
    ```bash
    chmod +x *.sh
    ```

---

## 💡 Fluxo de Trabalho (Como Usar)

Com o ambiente configurado, o uso diário é simplificado pelos scripts de atalho.

### 1. Treinando a IA

Sempre que você adicionar, alterar ou remover arquivos na pasta `data/`, execute o script de treinamento para atualizar a base de conhecimento do copiloto.
```bash
./treinar_ia.sh
```

### 2. Conversando com o Copiloto
Para iniciar o chat interativo no terminal e fazer perguntas sobre seu projeto:

```Bash
./ai_etl.sh
```

Para sair do chat, digite sair ou exit.