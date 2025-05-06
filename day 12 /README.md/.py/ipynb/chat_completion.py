import os
from dotenv import load_dotenv
import openai

load_dotenv()  # loads OPENAI_API_KEY from .env
openai.api_key = os.getenv("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")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
print(response.choices[0].message.content)
