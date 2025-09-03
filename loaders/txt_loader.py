from langchain_community.document_loaders import TextLoader

def load(file_path: str):
    """Carrega o conteúdo de um arquivo de texto."""
    print(f"INFO: Carregando TXT: {file_path}")
    loader = TextLoader(file_path, encoding='utf-8')
    return loader.load()