from flask import Flask, request, render_template_string
from openai import OpenAI
import os

# Substitua pela sua chave da API da OpenAI
client = OpenAI()

app = Flask(__name__)

# Página inicial com formulário
@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Game Sage - Assistente de Jogos</title>
    </head>
    <body>
        <h2>Game Sage - Seu Assistente Virtual para Jogos</h2>
        <form action="/process" method="post">
            <label for="question">Faça sua pergunta sobre jogos:</label><br>
            <input type="text" id="question" name="question" size="50"><br><br>
            <input type="submit" value="Enviar">
        </form>
    </body>
    </html>
    ''')

# Processa a pergunta e retorna a resposta da IA
@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['question']
    messages = [
        {"role": "system", "content": "Você se chama Game Sage. É um assistente virtual especialista na área de jogos, com um amplo conhecimento do mercado. Você só responde perguntas relacionadas a jogos."},
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    answer = response.choices[0].message
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Resposta do Game Sage</title>
    </head>
    <body>
        <h2>Sua Pergunta:</h2>
        <p>{{ user_input }}</p>
        <h2>Resposta do Game Sage:</h2>
        <p>{{ answer }}</p>
        <a href="/">Faça outra pergunta</a>
    </body>
    </html>
    ''', user_input=user_input, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
