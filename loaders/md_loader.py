from langchain_community.document_loaders import UnstructuredMarkdownLoader

def load(file_path: str):
    """Carrega o conteúdo de um arquivo Markdown."""
    print(f"INFO: Carregando Markdown: {file_path}")
    loader = UnstructuredMarkdownLoader(file_path)
    return loader.load()