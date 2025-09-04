# 🤖 AI Copilot - Serviço de ETL e RAG Genérico

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge\&logo=postgresql\&logoColor=white)
![NVIDIA](https://img.shields.io/badge/NVIDIA-CUDA-76B900?style=for-the-badge\&logo=nvidia\&logoColor=white)

Este projeto implementa um pipeline completo de **Retrieval-Augmented Generation (RAG)**, projetado para servir como o núcleo de um copiloto de IA para qualquer sistema web complexo.

Ele lê, processa e indexa uma base de conhecimento privada (documentação, código-fonte, diagramas) e fornece uma interface de consulta inteligente, capaz de responder perguntas complexas de forma precisa e com baixa taxa de alucinações, utilizando a API do **Google Gemini**.

---

## 📋 Principais Funcionalidades

* **Pipeline de ETL Modular:** Suporta múltiplos formatos de arquivo (`.pdf`, `.docx`, `.txt`, `.md`, `.php`, `.sql`).
* **Base de Conhecimento Vetorial:** Utiliza *sentence-transformers* para gerar embeddings de alta qualidade e **FAISS** para busca vetorial eficiente.
* **Aceleração por GPU:** Geração de embeddings e busca otimizadas via **CUDA**.
* **Persistência de Metadados:** Armazenamento de chunks e metadados em **PostgreSQL**.
* **Geração de Respostas com LLM:** Integração com a API do **Google Gemini**.
* **Ambiente Containerizado:** Execução completa via **Docker Compose**, garantindo portabilidade.

---

## 🛠️ Stack de Tecnologias

* **Linguagem:** Python 3.11
* **Orquestração:** Docker & Docker Compose
* **IA & Machine Learning:**

  * LangChain
  * Sentence Transformers (*all-MiniLM-L6-v2*)
  * FAISS-GPU & PyTorch
  * Google Generative AI (Gemini 1.5 Flash)
* **Banco de Dados:** PostgreSQL 15
* **Ambiente Base:** Imagem NVIDIA CUDA no Ubuntu 22.04

---

## 🚀 Configuração do Ambiente

### ✅ Pré-requisitos

* Git
* Docker Desktop
* WSL2 (para usuários Windows)
* Drivers NVIDIA com suporte a CUDA instalados no host

### 🔧 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/elcelsius/ai_etl_project.git
   cd ai_etl_project
   ```

2. **Configure as variáveis de ambiente:**
   Copie o arquivo de exemplo `.env.example` para `.env`:

   ```bash
   cp .env.example .env
   ```

   Em seguida, edite `.env` e preencha com suas credenciais, especialmente a `GOOGLE_API_KEY`.

3. **Popule a Base de Conhecimento:**
   Adicione os arquivos de documentação e código-fonte do seu projeto na pasta `data/`. O ETL irá escanear todas as subpastas recursivamente.

4. **Construa a Imagem Docker:**
   *Este passo pode demorar na primeira vez, pois baixa a imagem base da NVIDIA.*

   ```bash
   docker-compose build
   ```

5. **Dê permissão de execução aos scripts:**

   ```bash
   chmod +x *.sh
   ```

---

## 💡 Fluxo de Trabalho

### 1. Treinando a IA

Sempre que modificar arquivos na pasta `data/`, execute o script de treinamento para atualizar a base de conhecimento do copiloto:

```bash
./treinar_ia.sh
```

### 2. Conversando com o Copiloto

Para iniciar o chat interativo no terminal:

```bash
./iniciar_chat.sh
```

Para sair do chat, digite `sair` ou `exit` e pressione Enter.

---

## 📌 Observações

* O projeto foi otimizado para ambientes com GPU NVIDIA.
* Para rodar em ambiente sem GPU (apenas CPU):

  * No `requirements.txt`, substitua `faiss-gpu` por `faiss-cpu`.
  * No `docker-compose.yml`, remova a seção `deploy` do serviço `ai_api`.
  * O desempenho será consideravelmente mais lento.

---

<div align="center">
  <small>Desenvolvido por <strong>Celso Lisboa</strong></small>
  <br>
  <a href="https://github.com/elcelsius/ai_etl_project">Link para o Repositório</a>
</div>
