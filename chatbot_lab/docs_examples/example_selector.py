from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain import PromptTemplate, FewShotPromptTemplate

def example_selector(word):
    # These are a lot of examples of a pretend task of creating antonyms.
    examples = [
        {"word": "happy", "antonym": "sad"},
        {"word": "tall", "antonym": "short"},
        {"word": "energetic", "antonym": "lethargic"},
        {"word": "sunny", "antonym": "gloomy"},
        {"word": "windy", "antonym": "calm"},
    ]

    example_formatter_template = "Word: {word} \ Antonym: {antonym}"


    example_prompt = PromptTemplate(
        input_variables=["word", "antonym"],
        template=example_formatter_template,
    )

    example_selector = LengthBasedExampleSelector(
        # These are the examples is has available to choose from.
        examples=examples, 
        # This is the PromptTemplate being used to format the examples.
        example_prompt=example_prompt, 
        # This is the maximum length that the formatted examples should be.
        # Length is measured by the get_text_length function below.
        max_length=25,
    )

    # We can now use the `example_selector` to create a `FewShotPromptTemplate`.
    dynamic_prompt = FewShotPromptTemplate(
        # We provide an ExampleSelector instead of examples.
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix="Give the antonym of every input",
        suffix="Word: {input}\nAntonym:",
        input_variables=["input"],
        example_separator="\n",
    )

    # We can now generate a prompt using the `format` method.
    print(dynamic_prompt.format(input=word))
    # -> Give the antonym of every input
    # ->
    # -> Word: happy
    # -> Antonym: sad
    # ->
    # -> Word: tall
    # -> Antonym: short
    # ->
    # -> Word: energetic
    # -> Antonym: lethargic
    # ->
    # -> Word: sunny
    # -> Antonym: gloomy
    # ->
    # -> Word: windy
    # -> Antonym: calm
    # ->
    # -> Word: big