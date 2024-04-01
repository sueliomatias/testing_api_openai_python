import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

headers = { "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json" }

# listar modelos disponíveis
link = "https://api.openai.com/v1/models"
requisicao = requests.get(link, headers=headers)
print(requisicao.text)

# Fazer pergunta e obter resposta do modelo
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo" 

body_msg = {
    "model": id_modelo,
    "messages": [{
        "role": "user",
        "content": "O que é um LLM?"
    }]
}

body_msg = json.dumps(body_msg)

requisicao = requests.post(link, headers=headers, data=body_msg)
resposta = requisicao.json()
print(requisicao.text)


mensagem = resposta["choices"][0]['message']["content"]
print(mensagem)