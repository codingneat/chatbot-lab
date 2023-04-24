import os
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader

load_dotenv()

def get_github_source(repo_name):
    github_path = f"{os.getenv('DATA_PATH')}/github_support/{repo_name}"
    loader = DirectoryLoader(github_path, glob="*.md")
    return loader.load()
