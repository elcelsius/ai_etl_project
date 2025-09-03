from langchain_community.document_loaders import PyPDFLoader

def load(file_path: str):
    """Carrega o conteúdo de um arquivo PDF."""
    print(f"INFO: Carregando PDF: {file_path}")
    loader = PyPDFLoader(file_path)
    return loader.load()