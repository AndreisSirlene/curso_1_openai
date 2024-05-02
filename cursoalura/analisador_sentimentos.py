from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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
        
def analisador_sentimentos(produto):
    prompt_sistema = f"""
        You are a product review sentiment analyzer.
        Write a paragraph with up to 50 words summarizing the reviews and
        then assign the general sentiment for the product.
        Identify also 3 strengths and 3 weaknesses identified from the reviews.

        # Output Format
        Product Name:
        Review Summary:
        General Sentiment: [use only Positive, Negative, or Neutral]
        Strengths: list with three bullets
        Weaknesses: list with three bullets
    """

    prompt_usuario = carrega(r"data\\avaliacoes-" + produto + ".txt")
    print(f"Inicou a análise de sentimentos do produto {produto}")
    
    lista_mensagens = [
        {
            "role": "system",
            "content": prompt_sistema
        },
        {
            "role": "user",
            "content": prompt_usuario
        }
    ]
    
    response = cliente.chat.completions.create(
        messages= lista_mensagens,
        model= model
    )
    
    text_response = response.choices[0].message.content
    save(r"data\\analise-" + produto + ".txt", text_response)
    
analisador_sentimentos("Maquiagem mineral")
    