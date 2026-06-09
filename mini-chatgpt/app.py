from flask import Flask, render_template, request, jsonify
from ollama import chat

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def enviar_mensagem():

    dados = request.get_json()

    mensagem = dados["mensagem"]

    resposta = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )

    texto_resposta = resposta["message"]["content"]

    return jsonify({
        "resposta": texto_resposta
    })


app.run(debug=True)