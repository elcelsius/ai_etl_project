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

def get_db_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

def generate_answer(context: str, query: str):
    """Usa o Gemini para gerar uma resposta baseada no contexto e na pergunta."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    Você é um assistente de programação especialista no projeto. Sua tarefa é responder à pergunta do usuário de forma clara e concisa, utilizando APENAS as informações fornecidas no CONTEXTO abaixo. Não invente informações. Se a resposta não estiver no contexto, diga "Com base na minha documentação, não encontrei informações sobre isso."
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

def search_documents(query_text: str, embeddings_model, index, top_k: int = 5):
    """
    Função refatorada para receber o modelo e o índice já carregados.
    """
    # 1. Gera o embedding da pergunta
    query_embedding = embeddings_model.embed_query(query_text)
    query_vector = np.array([query_embedding], dtype=np.float32)

    # 2. Busca no FAISS
    distances, ids = index.search(query_vector, top_k)
    
    if not ids.any():
        return "Desculpe, não encontrei nenhum documento relevante para sua pergunta."
        
    faiss_indices = tuple(int(i) for i in ids[0])
    
    # 3. Busca no PostgreSQL
    conn = get_db_connection()
    cur = conn.cursor()
    query_sql = "SELECT source_file, chunk_text FROM document_chunks WHERE faiss_index IN %s"
    cur.execute(query_sql, (faiss_indices,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    # 4. Monta o contexto e gera a resposta final com o Gemini
    context_text = "\n\n".join([f"Trecho do arquivo {row[0]}:\n{row[1]}" for row in results])
    final_answer = generate_answer(context_text, query_text)
    return final_answer

def main():
    """
    Função principal que carrega os modelos e inicia o loop do chat interativo.
    """
    print("--- Carregando modelos... Aguarde. ---")
    
    # Carrega os modelos e o índice UMA ÚNICA VEZ
    embeddings_model = HuggingFaceEmbeddings(model_name=MODEL_NAME, model_kwargs={'device': DEVICE})
    index = faiss.read_index(f"{VECTOR_STORE_PATH}/index.faiss")
    
    print("\n" + "="*50)
    print("🤖 Copiloto ReurbSys pronto! Faça sua pergunta.")
    print("   Digite 'sair', 'exit' ou 'quit' para terminar.")
    print("="*50)

    # Inicia o loop do chat
    while True:
        try:
            query = input("🤖 Você: ")
            if query.lower() in ["sair", "exit", "quit"]:
                print("\nAté a próxima!")
                break
            
            if not query.strip():
                continue

            print("🧠 Pensando...")
            answer = search_documents(query, embeddings_model, index)
            
            print("\n" + "="*50)
            print("🤖 Copiloto:")
            print(answer)
            print("="*50 + "\n")

        except (KeyboardInterrupt, EOFError):
            print("\nAté a próxima!")
            break

if __name__ == "__main__":
    main()