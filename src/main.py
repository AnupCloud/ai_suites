from typing import List, Tuple
import aisuite as ai
from dotenv import load_dotenv
from config import CREDENTIALS


# Load credentials from environment file
load_dotenv(dotenv_path=CREDENTIALS)

# Initialize AI Suite client
client = ai.Client()


def fetch_aisuite_responses(models: List[str], prompt: str) -> List[Tuple[str, str]]:
    """
    Fetch responses from AISuite models.

    :param models: A list of model identifiers (strings).
    :param prompt: The user's prompt/question.
    :return: A list of tuples where each tuple contains the model name and its response.
    """
    # Prepare the conversation messages
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant"},
        {"role": "user", "content": prompt}
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
        "ollama:llama3.2",
        "ollama:phi4"
    ]
    prompt = "tell me something about Agentic AI in 1 line"
    # Fetch responses for each model
    responses = fetch_aisuite_responses(ai_models, prompt)

    # Print the results in a readable format
    for model_name, model_output in responses:
        print(f"Model: {model_name}")
        print("Output:")
        print(model_output)
        print("-" * 40)  # separator for readability


if __name__ == "__main__":
    main()

