from langchain_community.document_loaders import Docx2txtLoader

def load(file_path: str):
    """Carrega o conteúdo de um arquivo DOCX."""
    print(f"INFO: Carregando DOCX: {file_path}")
    loader = Docx2txtLoader(file_path)
    return loader.load()