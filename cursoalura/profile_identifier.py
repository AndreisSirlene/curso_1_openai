from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo-1106"

codificador = tiktoken.encoding_for_model(modelo)

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")


prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("data\lista_de_compras_100_clientes.csv")

lista_de_tokens = codificador.encode(prompt_sistema + prompt_usuario)
numero_de_tokens = len(lista_de_tokens)
print(f"Número de tokens na entrada: {numero_de_tokens}")
tamanho_esperado_saida = 2048

if numero_de_tokens >= 4096 - tamanho_esperado_saida:
    modelo = "gpt-4" #"gpt-4-1106-preview"

print(f"Modelo escolhido: {modelo}")

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

resposta = client.chat.completions.create(
    messages = lista_mensagens,
    model=modelo
)

print(resposta.choices[0].message.content)

#Aqui aprendemos a selecionar o modelo de linguagem adequado para nossas tarefas e como utilizar a biblioteca TikToken 
# para contar e estimar a quantidade de tokens em texto e implementar em nosso código um modo de selecionar o modelo utilizado de GPT, de acordo com nossa necessidade.

#Definir os limites para tomar a decisão da escolha de um novo modelo é uma tarefa que cabe à pessoa que está projetando 
# a solução. Desta forma, embora o nosso corte tenha sido apenas para 4.096 tokens, você pode atualizar seu código para apenas trocar o modelo quando atingir o limite de tokens!