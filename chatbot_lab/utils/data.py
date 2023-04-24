from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def split_source(sources):
    source_chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
    for source in sources:
        for chunk in splitter.split_text(source.page_content):
            source_chunks.append(Document(page_content=chunk, metadata=source.metadata))
    return source_chunks