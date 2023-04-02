import os

import openai
from dotenv import load_dotenv

load_dotenv()

model_engine = "text-davinci-003"

openai.api_key = os.getenv("OPENAI_API_KEY")


def send_message_to_gpt(message):
    response = openai.Completion.create(
        model=model_engine,
        prompt=message,
        max_tokens=1024,
        temperature=0.7,
        stop=None,
    )
    return response.choices[0].text.strip()
