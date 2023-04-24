from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv

from chatbot_lab.utils.api import get_wiki_data

load_dotenv()


def run_wiki_paragraph(question):
    sources = [
        get_wiki_data("Cloud_computing", True),
        get_wiki_data("Roger_Federer", True),
        get_wiki_data("Rafael_Nadal", True),
        get_wiki_data("Seinfeld", True),
    ]

    chain = load_qa_with_sources_chain(OpenAI(temperature=0))
    
    print(
        chain(
            {
                "input_documents": sources,
                "question": question,
            },
            return_only_outputs=True,
        )["output_text"]
    )