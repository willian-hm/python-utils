from flask import Flask, render_template, request, jsonify
from ollama import chat
import json
import os

MEMORIA_FILE = "memoria.json"

def carregar_memoria():
    if not os.path.exists(MEMORIA_FILE):
        return {"mensagens": []}

    with open(MEMORIA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_memoria(memoria):
    with open(MEMORIA_FILE, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=4)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def enviar_mensagem():
    dados = request.get_json()
    mensagem = dados["mensagem"]

    memoria = carregar_memoria()

    memoria["mensagens"].append({
        "role": "user",
        "content": mensagem
    })

    memoria["mensagens"] = memoria["mensagens"][-20:]

    resposta = chat(
        model="llama3",
        messages=memoria["mensagens"]
    )

    texto_resposta = resposta["message"]["content"]

    # adiciona resposta da IA na memória
    memoria["mensagens"].append({
        "role": "assistant",
        "content": texto_resposta
    })

    salvar_memoria(memoria)

    return jsonify({
        "resposta": texto_resposta
    })


app.run(debug=True)