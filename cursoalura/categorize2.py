from openai import OpenAI 
import os
from dotenv import load_dotenv

load_dotenv()
cliente = OpenAI(api_key=os.getenv("openai_api_key"))
model = "gpt-3.5-turbo-1106" #"gpt-4"

def categorize_product(product_name, list_categories):
    system_promt = f"""
    You are a product categorizer.
    You should assume the categories listed below.

    # List of Valid Categories
    {list_categories.split(",")}

    # Output Format
    Product: Product Name
    Category: display the product category

    # Example of Output
    Product: Solar charging electric brush
    Category: Green Electronics
    """


    answer = cliente.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_promt
            },
            {
                "role": "user",
                "content": product_name
            
            }
        ],
        model = model,
        temperature = 0,
        max_tokens = 200
    )
    return answer.choices[0].message.content
   
valid_categories = input("Inform the valid categories, split by comma: ")  

while True:
    product_name = input,
    respost_text = categorize_product(product_name, valid_categories)
    print(respost_text)
    
    