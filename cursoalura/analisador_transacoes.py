from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

def carrega(file_name):
    try:
        with open(file_name, "r") as archive:
            dados = archive.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")
        
def save(file_name, conteudo):
    try:
        with open(file_name, "w", encoding="utf-8") as archive:
            archive.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")
        
def analise_transacao(list_transactions):
    print("1. Executing Transaction analyses")
    
    prompt_sistema = """
    Analyze the following financial transactions and identify whether each one is a "Possible Fraud" or should be "Approved".
    Add a "Status" attribute with one of the values: "Possible Fraud" or "Approved".

    Each new transaction should be inserted into the JSON list.

    # Possible indicators of fraud
    Transactions with highly discrepant values
    Transactions that occur in locations very far from each other.
    Adopt the response format below to compose your answer.
    
    # Output Format
    {
        "transactions": [
            {
            "id": "id",
            "type": "credit or debit",
            "establishment": "name of the establishment",
            "time": "transaction time",
            "value": "R$XX,XX",
            "product_name": "name of the product",
            "location": "city - state (Country)"
            "status": ""
            },
        ]
    }
"""
    lista_mensagens = [
            {
                    "role": "system",
                    "content": prompt_sistema
            },
            {
                    "role": "user",
                    "content": f"""Consider the below CSV, where each row is a different transaction: {list_transactions}.
                    Your answer should adopt the  #Output Format (only a json without any other comment)"""
            }]    


    resposta = client.chat.completions.create(
        messages = lista_mensagens,
        model=model,
        temperature=0
)

    conteudo = resposta.choices[0].message.content.replace("'", '"')
    print("\Conteúdo:", conteudo)
    json_resultado = json.loads(conteudo)
    print("\nJSON:", json_resultado)
    return json_resultado

def create_review(transaction):
    print("2. Generating a review for each transaction", transaction["id"])

    prompt_system = f"""
    For the following transaction, provide an review, only if its status is "Possible Fraud".
    Indicate in the review a justification for identifying a fraud.
    Transaction: {transaction}

    ## Response Format
    "id": "id",
    "type": "credit or debit",
    "establishment": "name of the establishment",
    "time": "transaction time",
    "value": "R$XX,XX",
    "product_name": "name of the product",
    "location": "city - state (Country)"
    "status": "",
    "opinion": "Place Not Applicable if the status is Approved"
    """
    lista_mensagens = [
        {
            "role": "system",
            "content": prompt_system
        }
    ]

    resposta = client.chat.completions.create(
        messages = lista_mensagens,
        model=model,
    )

    conteudo = resposta.choices[0].message.content
    print("Completed the analyses:")
    return conteudo

def generate_recommendations(review):
    print("3. Generating recommendations")
    
    prompt_system = f"""
    For the following transaction, provide an appropriate recommendation based on the status and details of the Transaction: {opinion}

    Recommendations can be "Notify Customer", "Activate Anti-Fraud Department", or "Perform Manual Verification".
    They should be written in a technical format.

    Also include a classification of the type of fraud, if applicable.
    """
    
    lista_mensagens = [
        {
            "role": "system",
            "content": prompt_system
        }
    ]

    resposta = client.chat.completions.create(
        messages = lista_mensagens,
        model=model,
    )
    
    conteudo = resposta.choices[0].message.content
    print("Complete the recommendation:")
    return conteudo


list_transactions = carrega(r"data\\transacoes.csv")
transaction_analised = analise_transacao(list_transactions)

for transaction in transaction_analised["transacoes"]:
    if transaction["status"] == "Possible Fraud":
        review = create_review(transaction)
        recommendation = generate_recommendations(review)
        id_transaction = transaction["id"]
        producto_transaction = transaction["nome_produto"]
        status_transaction = transaction["status"]
        save(f"transacoes-{id_transaction}-{producto_transaction}-{status_transaction}.txt", recommendation)
    

