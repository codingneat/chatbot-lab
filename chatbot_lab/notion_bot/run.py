import os
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from langchain.chains.llm import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.document_loaders import NotionDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
from dotenv import load_dotenv

from chatbot_lab.utils.history import retrieve_history, save_history

load_dotenv()


def run_notion_chat(question):
    loader = NotionDirectoryLoader(
        f"{os.getenv('DATA_PATH')}/notion_data"
    )
    raw_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    documents = text_splitter.split_documents(raw_documents)
    search_index = FAISS.from_documents(documents, OpenAIEmbeddings())
    doc_chain = load_qa_with_sources_chain(OpenAI(temperature=0))
    question_generator = LLMChain(llm=OpenAI(temperature=0), prompt=CONDENSE_QUESTION_PROMPT)
 
    chat_history = retrieve_history()
    

    chain = ConversationalRetrievalChain(
        retriever=search_index.as_retriever(),
        question_generator=question_generator,
        combine_docs_chain=doc_chain,
    )

    chain_result = chain({
            "question": question,
            "chat_history": chat_history
        },
    )

    save_history(question, chain_result["answer"])

    print(chain_result["answer"])
 