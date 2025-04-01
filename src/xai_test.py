import aisuite as ai
from dotenv import load_dotenv

load_dotenv()
client = ai.Client()

models = ["xai:grok-2-latest"]


messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)