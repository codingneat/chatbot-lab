import click

from chatbot_lab.wiki.wiki_paragraph.run import run_wiki_paragraph
from chatbot_lab.wiki.wiki_page_fr.run import run_wiki_page_fr
from chatbot_lab.wiki.wiki_page.run import run_wiki_page
from chatbot_lab.support.support_github.run import run_github_support
from chatbot_lab.pdf_bot.run import run_pdf_bot
from chatbot_lab.support.support_docs.run import run_docs_support
from chatbot_lab.docs_examples.prompt_template import prompt_template
from chatbot_lab.docs_examples.example_selector import example_selector
from chatbot_lab.notion_bot.run import run_notion_chat


@click.group()
def main():
    pass


@main.command()
@click.option("--paragraph", "wiki_type", flag_value="paragraph", default=True)
@click.option("--page", "wiki_type", flag_value="page")
@click.option("--pagefr", "wiki_type", flag_value="page_fr")
@click.option(
    "--question", prompt="Your question", help="Ask a question to wiki chatbot"
)
def wiki_chat(wiki_type, question):
    if wiki_type == "page":
        run_wiki_page(question)
    elif wiki_type == "page_fr":
        run_wiki_page_fr(question)
    else:
        run_wiki_paragraph(question)


@main.command()
@click.option("--github", "support_type", flag_value="github", default=True)
@click.option("--docs", "support_type", flag_value="docs")
@click.option(
    "--question", prompt="Your question", help="Ask a question to support chatbot"
)
def support_chat(support_type, question):
    if support_type == "github":
        run_github_support(question)
    else:
        run_docs_support(question)

@main.command()
@click.option(
    "--question", prompt="Your question", help="Ask a question to notion chatbot"
)
def notion_chat(question):
    run_notion_chat(question)


@main.command()
@click.option(
    "--product", prompt="Your product", help="Choose a product to pass to the prompting template"
)
def use_prompt(product):
    prompt_template(product)

@main.command()
@click.option(
    "--word", prompt="Your word", help="Choose a word to pass to the prompting template"
)
def use_example_selector(word):
    example_selector(word)


@main.command()
@click.option(
    "--question", prompt="Your question", help="Ask a question to pdf chatbot"
)
def pdf_chat(question):
    run_pdf_bot(question)


if __name__ == "__main__":
    main()
