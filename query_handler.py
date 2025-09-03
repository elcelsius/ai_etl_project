import os
import torch
import psycopg2
import faiss
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- CONFIGURAÇÃO DA API DO GEMINI ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("A chave de API do Google não foi encontrada. Verifique seu arquivo .env")
genai.configure(api_key=GOOGLE_API_KEY)

# --- CONFIGURAÇÕES GERAIS ---
VECTOR_STORE_PATH = "vector_store/faiss_index"
MODEL_NAME = "all-MiniLM-L6-v2"
DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"--- Usando dispositivo de embedding: {DEVICE} ---")

def get_db_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

def generate_answer(context: str, query: str):
    """
    Usa o Gemini para gerar uma resposta baseada no contexto e na pergunta.
    """
    print("\nINFO: Enviando contexto e pergunta para o Gemini...")
    
    # Escolha do modelo Gemini. 'gemini-1.5-flash' é rápido e eficiente.
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Este é o nosso prompt de RAG. Ele instrui o modelo a se comportar como queremos.
    prompt = f"""
    Você é um assistente de programação especialista no projeto ReurbSys. Sua tarefa é responder à pergunta do usuário de forma clara e concisa, utilizando APENAS as informações fornecidas no CONTEXTO abaixo. Não invente informações. Se a resposta não estiver no contexto, diga "Com base na minha documentação, não encontrei informações sobre isso."

    CONTEXTO:
    ---
    {context}
    ---

    PERGUNTA DO USUÁRIO:
    {query}

    RESPOSTA:
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Ocorreu um erro ao chamar a API do Gemini: {e}"

def search_documents(query_text: str, top_k: int = 5):
    """
    Realiza a busca vetorial (Retrieval) e depois chama o LLM para gerar a resposta final (Generation).
    """
    print(f"INFO: Carregando modelo de embeddings '{MODEL_NAME}'...")
    embeddings_model = HuggingFaceEmbeddings(model_name=MODEL_NAME, model_kwargs={'device': DEVICE})

    print(f"INFO: Carregando índice FAISS de '{VECTOR_STORE_PATH}'...")
    index = faiss.read_index(f"{VECTOR_STORE_PATH}/index.faiss")

    print(f"\n--- BUSCANDO pela pergunta: '{query_text}' ---")
    query_embedding = embeddings_model.embed_query(query_text)
    query_vector = np.array([query_embedding], dtype=np.float32)
    distances, ids = index.search(query_vector, top_k)
    
    if not ids.any():
        print("Nenhum documento relevante encontrado.")
        return
        
    faiss_indices = tuple(int(i) for i in ids[0])
    
    print("INFO: Buscando textos completos no PostgreSQL...")
    conn = get_db_connection()
    cur = conn.cursor()
    query_sql = "SELECT source_file, chunk_text FROM document_chunks WHERE faiss_index IN %s"
    cur.execute(query_sql, (faiss_indices,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    # Monta o contexto a partir dos resultados da busca
    context_text = "\n\n".join([f"Trecho do arquivo {row[0]}:\n{row[1]}" for row in results])
    
    # --- A MÁGICA FINAL ---
    # Envia o contexto e a pergunta para o Gemini gerar a resposta
    final_answer = generate_answer(context_text, query_text)
    
    print("\n" + "="*50)
    print("🤖 RESPOSTA DO COPILOTO REURBSYS 🤖")
    print("="*50)
    print(final_answer)
    print("="*50)


if __name__ == "__main__":
    # <<-- AQUI VOCÊ PODE MUDAR A PERGUNTA PARA TESTAR -->>
    pergunta_exemplo = "Qual a estrutura da tabela de usuários no banco de dados landlord?"
    # Outros exemplos para testar:
    # pergunta_exemplo = "Como funciona a arquitetura multi-tenant?"
    # pergunta_exemplo = "Qual a stack de tecnologia do projeto?"
    
    search_documents(pergunta_exemplo)