# 🤖 AI Copilot – Serviço de ETL e RAG

Este projeto implementa um pipeline completo de **Retrieval-Augmented Generation (RAG)**, projetado para servir como núcleo de um copiloto de IA em sistemas web complexos.

O objetivo é **ler, processar e indexar** uma base de conhecimento privada (documentação, código-fonte, diagramas, regulamentos, etc.) e fornecer uma **interface de consulta inteligente**, capaz de responder perguntas complexas de forma precisa e contextualizada, utilizando a API do **Google Gemini**.

Essa abordagem reduz significativamente o risco de **alucinações em LLMs** ao combinar a busca em dados vetorizados com a geração de respostas.

---

## 📋 Principais Funcionalidades

* **Pipeline de ETL Modular** – processa múltiplos formatos de arquivo (`.pdf`, `.docx`, `.txt`, `.md`, além de arquivos de código como `.php`, `.sql`).
* **Base de Conhecimento Vetorial** – utiliza `sentence-transformers` para gerar embeddings de alta qualidade e `FAISS` para indexação e busca vetorial eficiente.
* **Aceleração por GPU** – suporte a CUDA para acelerar embeddings e buscas, garantindo alta performance.
* **Persistência de Metadados** – chunks de texto e seus metadados são armazenados em **PostgreSQL** para consistência e referência futura.
* **Integração com LLM** – respostas geradas com a API do **Google Gemini**, utilizando o contexto recuperado da base de conhecimento.
* **Ambiente Containerizado** – execução em **Docker** e **Docker Compose**, facilitando portabilidade e configuração.

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

### Pré-requisitos

* Git
* Docker Desktop
* WSL2 (para usuários Windows)
* Drivers NVIDIA com suporte a CUDA instalados no host

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/elcelsius/ai_etl_project.git
   cd ai_etl_project
   ```

2. **Configure as variáveis de ambiente:**

   ```bash
   cp .env.example .env
   ```

   Em seguida, edite o arquivo `.env` e adicione suas credenciais, em especial a `GOOGLE_API_KEY`.

3. **Popule a base de conhecimento:**
   Coloque seus arquivos (documentação, código, regulamentos, etc.) na pasta `data/`.
   O ETL fará a varredura recursiva em todas as subpastas.

4. **Construa a imagem Docker:**

   ```bash
   docker-compose build
   ```

---

## 💡 Como Usar

### 1. Executando o Pipeline de ETL

Para processar os arquivos da pasta `data/` e recriar a base de conhecimento:

```bash
docker-compose run --rm etl python3 etl_orchestrator.py
```

---

## 🌐 Possíveis Aplicações

Embora tenha sido desenvolvido como solução genérica de **ETL + RAG**, este projeto pode ser adaptado para diferentes cenários:

* **Chatbots institucionais (universidades, órgãos públicos, ONGs)**

  * Responder dúvidas sobre cursos, regulamentos, calendário acadêmico e serviços.
  * Apoiar estudantes, docentes e funcionários com informações rápidas e acessíveis.
  * Centralizar informações que normalmente estão espalhadas em portais e documentos.

* **Documentação técnica e empresarial**

  * Ajudar equipes internas a consultar manuais, APIs, diagramas e código-fonte.
  * Reduzir tempo de treinamento de novos colaboradores.

* **Suporte ao cliente**

  * Responder dúvidas frequentes em sites e sistemas de atendimento.
  * Oferecer experiências personalizadas e em tempo real.


---

## 📌 Status do Projeto

* [x] Pipeline ETL funcional
* [x] Integração com embeddings e FAISS
* [x] Integração com Google Gemini
* [ ] Interface de consulta web (em desenvolvimento)
* [ ] Integração com canais externos (site institucional, WhatsApp, etc.)

---

## 🤝 Contribuições

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

---

## 📄 Licença

Este projeto está sob a licença MIT – consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

👉 Assim o README fica técnico para devs, mas também **institucional** para quem quer avaliar aplicações reais (como a DTI).

Quer que eu já crie também uma **versão em inglês** do README (útil se você pensa em abrir para colaboração internacional no GitHub)?
