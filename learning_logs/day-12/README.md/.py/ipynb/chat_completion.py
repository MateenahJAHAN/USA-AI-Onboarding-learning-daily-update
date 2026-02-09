import os
from dotenv import load_dotenv
import openai

load_dotenv()  # loads OPENAI_API_KEY from .env
openai.api_key = os.getenv(secret_key)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
print(response.choices[0].message.content)
