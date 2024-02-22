from openai import OpenAI

# Inicializa o cliente OpenAI (Ajuste a linha abaixo conforme a maneira correta de autenticar com a chave da API)
client = OpenAI()

# Define as mensagens iniciais, incluindo a descrição do sistema
messages = [
    {"role": "system", "content": "Você se chama Game Sage. É um assistente virtual especialista na área de jogos, com um amplo conhecimento do mercado."},
]

# Pede ao usuário para digitar sua pergunta
user_input = input("Faça sua pergunta sobre jogos: ")

# Adiciona a pergunta do usuário às mensagens
messages.append({"role": "user", "content": user_input})

# Cria a conclusão com a pergunta do usuário
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=messages
)

# Imprime a resposta gerada pela IA
print(completion.choices[0].message)
