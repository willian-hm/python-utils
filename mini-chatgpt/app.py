from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()

    mensagem = dados["mensagem"]

    resposta = f"Você disse: {mensagem}"

    return jsonify({
        "resposta": resposta
        })

app.run(debug=True)