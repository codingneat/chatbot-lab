import os
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv

from chatbot_lab.utils.data import split_source

load_dotenv()


def run_pdf_bot(question):
    loader = PyPDFLoader(f"{os.getenv('DATA_PATH')}/pdf/chemical_enegergetics.pdf")
    pages = loader.load_and_split()
    source_chunks = split_source(pages)
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
