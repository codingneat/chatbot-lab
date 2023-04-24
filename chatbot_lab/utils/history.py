import jsonlines
import os
from dotenv import load_dotenv

load_dotenv()


def retrieve_history():
    with jsonlines.open(f"{os.environ['DATA_PATH']}/history.jsonl") as reader:
        return [(obj["question"], obj["answer"]) for obj in reader]


def save_history(question, answer):
    with jsonlines.open(f"{os.environ['DATA_PATH']}/history.jsonl", "a") as writer:
        writer.write({"question": question, "answer": answer})
