import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                                      # loads .env
client = OpenAI()                                  # picks up OPENAI_API_KEY

response = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    messages=[
        {"role": "user", "content": "Say hello in one short sentence."}
    ],
)

print(response.choices[0].message.content.strip())
