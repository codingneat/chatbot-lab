import pathlib
import subprocess
import tempfile
import os
import shutil
import subprocess
from dotenv import load_dotenv

load_dotenv()

def get_github_docs(repo_owner, repo_name):
    with tempfile.TemporaryDirectory() as d:
        subprocess.check_call(
            f"git clone --depth 1 https://github.com/{repo_owner}/{repo_name}.git .",
            cwd=d,
            shell=True,
        )
        git_sha = (
            subprocess.check_output("git rev-parse HEAD", shell=True, cwd=d)
            .decode("utf-8")
            .strip()
        )
        repo_path = pathlib.Path(d)
        markdown_files = list(repo_path.glob("*/*.md")) + list(
            repo_path.glob("*.md")
        )

        github_path = f"{os.getenv('DATA_PATH')}/github_support/{repo_name}"
        for markdown_file in markdown_files:
            isExist = os.path.exists(github_path)
            if not isExist:
                os.makedirs(github_path)
            head, tail = os.path.split(markdown_file)
            shutil.copyfile(markdown_file, f"{github_path}/{tail}")

        with open(f"{github_path}/sha.txt", "w") as f:
            f.write(git_sha)


get_github_docs("openai", "openai-cookbook")