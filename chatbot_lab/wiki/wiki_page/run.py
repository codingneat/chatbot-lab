from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from dotenv import load_dotenv

from chatbot_lab.utils.api import get_wiki_data

load_dotenv()

def run_wiki_page(question):
    sources = [
        get_wiki_data("Lisp_(programming_language)", False),
        get_wiki_data("Perl", False),
        get_wiki_data("PHP", False),
        get_wiki_data("CPython", False),
        get_wiki_data("Python_(programming_language)", False),
        get_wiki_data("Haskell", False),
    ]

    source_chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
    for source in sources:
        for chunk in splitter.split_text(source.page_content):
            source_chunks.append(Document(page_content=chunk, metadata=source.metadata))


    search_index = FAISS.from_documents(source_chunks, OpenAIEmbeddings())

    chain = load_qa_with_sources_chain(OpenAI(temperature=0))

    print(
        chain(
            {
                "input_documents": search_index.similarity_search(question, k=4),
                "question": question,
            },
            return_only_outputs=True,
        )["output_text"]
    )