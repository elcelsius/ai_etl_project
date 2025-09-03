from langchain_community.document_loaders import TextLoader

def load(file_path: str):
    """
    Carrega o conteúdo de arquivos de código ou texto plano,
    tratando possíveis erros de encoding.
    """
    print(f"INFO: Carregando arquivo de código/texto: {file_path}")
    try:
        loader = TextLoader(file_path, encoding='utf-8')
        return loader.load()
    except Exception as e:
        print(f"WARNING: Falha ao carregar {file_path} com UTF-8: {e}. Tentando com 'latin-1'.")
        try:
            loader = TextLoader(file_path, encoding='latin-1')
            return loader.load()
        except Exception as e2:
            print(f"ERROR: Falha ao carregar {file_path} com todos os encodings tentados: {e2}")
            return []