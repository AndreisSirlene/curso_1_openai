from openai import OpenAI 
import os
from dotenv import load_dotenv

load_dotenv()
cliente = OpenAI(api_key=os.getenv("openai_api_key"))
model = "gpt-3.5" 


system_promt = f"""
You are a product categorizer.
You should assume the categories listed below.

# List of Valid Categories
   - Sustainable Fashion
   - Home Products
   - Natural Beauty
   - Green Electronics

# Output Format
Product: Product Name
Category: display the product category

# Example of Output
Product: Solar charging electric brush
Category: Green Electronics
"""
user_prompt = input("Here's a product name: ")


answer = cliente.chat.completions.create(
    messages = [
        {
            "role": "system",
            "content": system_promt
        },
        {
            "role": "user",
            "content": user_prompt
          
        }
    ],
    model = model,
    temperature = 0,
    max_tokens = 200
    #n= 2
)
#Considerando que aqui n#ao estamos buscando o retorno de v]arias respostas comentamos o (n:numero de respostas) e o loop.
#for r in range(0,2):
    #print(answer.choices[r].message.content)
    

print(answer.choices[0].message.content)