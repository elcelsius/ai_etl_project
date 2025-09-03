# 🤖 AI Copilot - Serviço de ETL e RAG Genérico

Este projeto implementa um pipeline completo de **Retrieval-Augmented Generation (RAG)**, projetado para servir como o núcleo de um copiloto de IA para sistemas web complexos.

O objetivo é **ler, processar e indexar** uma base de conhecimento privada (documentação, código-fonte, diagramas) e fornecer uma interface de consulta inteligente, capaz de responder perguntas complexas de forma precisa e com baixa taxa de alucinações, utilizando a API do **Google Gemini**.

---

## 📋 Principais Funcionalidades
- **Pipeline de ETL Modular**: suporta múltiplos formatos de arquivo (.pdf, .docx, .txt, .md, .php, .sql).
- **Base de Conhecimento Vetorial**: utiliza *sentence-transformers* para gerar embeddings de alta qualidade e **FAISS** para busca vetorial eficiente.
- **Aceleração por GPU**: geração de embeddings e busca otimizadas via **CUDA**.
- **Persistência de Metadados**: armazenamento de chunks e metadados em **PostgreSQL**.
- **Geração de Respostas com LLM**: integração com a API do **Google Gemini**.
- **Ambiente Containerizado**: execução completa via **Docker Compose**, garantindo portabilidade.

---

## 🛠️ Stack de Tecnologias
- **Linguagem**: Python 3.11  
- **Orquestração**: Docker & Docker Compose  
- **IA & Machine Learning**:  
  - LangChain  
  - Sentence Transformers (*all-MiniLM-L6-v2*)  
  - FAISS-GPU  
  - PyTorch  
  - Google Generative AI (Gemini 1.5 Flash)  
- **Banco de Dados**: PostgreSQL 15  
- **Ambiente Base**: Imagem NVIDIA CUDA no Ubuntu 22.04  

---

## 🚀 Configuração do Ambiente

### ✅ Pré-requisitos
- Git  
- Docker Desktop  
- WSL2 (para usuários Windows)  
- Drivers NVIDIA com suporte a CUDA instalados no host  

### 🔧 Instalação

Clone o repositório:
```bash
git clone https://github.com/elcelsius/ai_etl_project.git
cd ai_etl_project
```

Configure as variáveis de ambiente:  
Copie o arquivo de exemplo `.env.example` para `.env`:
```bash
cp .env.example .env
```

Edite o arquivo `.env` e preencha com suas credenciais, especialmente sua **GOOGLE_API_KEY**.  

Exemplo de configuração:

```dotenv
# Credenciais do Banco de Dados PostgreSQL
POSTGRES_DB=ai_project
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Chave de API para o Google Gemini
# Obtenha sua chave em: https://aistudio.google.com/app/apikey
GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Adicione seus arquivos de documentação e código-fonte do projeto na pasta `data/`.  
👉 O ETL irá escanear todas as subpastas recursivamente.  

Construa a imagem Docker (pode demorar na primeira vez, pois baixa a imagem base da NVIDIA):
```bash
docker-compose build
```

Dê permissão de execução para os scripts:
```bash
chmod +x *.sh
```

---

## 💡 Fluxo de Trabalho (Como Usar)

### 1. Treinando a IA
Sempre que modificar arquivos na pasta `data/`, execute o script de treinamento para atualizar a base de conhecimento do copiloto:
```bash
./treinar_ia.sh
```

### 2. Conversando com o Copiloto
Para iniciar o chat interativo no terminal e fazer perguntas sobre seu projeto:
```bash
./ai_etl.sh
```

Para sair do chat, digite:
```
sair
```
ou
```
exit
```

---

## 📌 Observações
- O projeto foi otimizado para ambientes com GPU NVIDIA.  
- Caso não possua GPU, será necessário ajustar a configuração para uso apenas em CPU (com menor performance).  

---

✍️ Autor: **Celso Lisboa**  
📎 Repositório: [github.com/elcelsius/ai_etl_project](https://github.com/elcelsius/ai_etl_project)  
