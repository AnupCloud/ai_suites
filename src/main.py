from typing import List, Tuple
import aisuite as ai
from dotenv import load_dotenv
from src.config import CREDENTIALS


# Load credentials from environment file
load_dotenv(dotenv_path=CREDENTIALS)

# Initialize AI Suite client
client = ai.Client()


def fetch_aisuite_responses(models: List[str]) -> List[Tuple[str, str]]:
    """
    Fetch responses from AISuite models.

    :param models: A list of model identifiers (strings).
    :type models: List[str]
    :return: A list of tuples where each tuple contains the model name and its response.
    :rtype: List[Tuple[str, str]]

    Example return:
    [
        ("openai:o1", "Here is the response from openai:o1..."),
        ("anthropic:claude-3-5-haiku-latest", "Here is the response from Claude..."),
        ...
    ]
    """
    # Prepare the conversation messages
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant"},
        {"role": "user", "content": "tell me a joke on christmas"}
    ]

    results = []
    for model in models:
        # Create a completion request for each model
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=1,
        )
        data = response.choices[0].message.content
        results.append((model, data))

    return results


def main() -> None:
    """
    Main function to demonstrate fetching and printing AISuite responses.
    """
    ai_models = [
        "openai:o1",
        "anthropic:claude-3-5-haiku-latest",
        "google:gemini-2.0-flash-exp",
        "ollama:llama3.2"
    ]

    # Fetch responses for each model
    responses = fetch_aisuite_responses(ai_models)

    # Print the results in a readable format
    for model_name, model_output in responses:
        print(f"Model: {model_name}")
        print("Output:")
        print(model_output)
        print("-" * 40)  # separator for readability


if __name__ == "__main__":
    main()
