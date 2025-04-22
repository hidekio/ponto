from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resposta", methods=["POST"])
def resposta():
    nome = request.form["nome"]
    mensagem = f"Olá, {nome}! Obrigado por visitar a página."
    return render_template("index.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
