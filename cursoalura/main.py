from openai import OpenAI 
import os
from dotenv import load_dotenv


load_dotenv()
cliente = OpenAI(api_key=os.getenv("openai_api_key"))

answer = cliente.chat.completions.create(
    messages = [
        {
            "role": "system",
            "content": "List only the product names, without their description"
        },
        {
            "role": "user",
            "content": "List 3 sustenability products"
        }
    ],
    model ="gpt-4"
)

print(answer.choices[0].message.content)