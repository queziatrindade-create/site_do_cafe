# Importamos a nova função
from flask import Flask, render_template

app = Flask(__name__)

# --- Rota Principal ---
@app.route("/")
def index():
    # Em vez de retornar HTML, renderizamos o arquivo
    return render_template("index.html")

# --- Rota Sobre ---
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# --- Rota Contato ---
@app.route("/contato")
def contato():
    return "<h1>Contato</h1><p>Nosso email é professor@escola.com</p>"

# --- Rota Dinâmica Perfil ---
@app.route("/perfil/<nome>")
def perfil(nome):
    # Passamos a variável 'nome' do Python
    # para a variável 'nome_do_usuario' do template
    return render_template("perfil.html", nome_do_usuario=nome)


if __name__ == "__main__":
    app.run(debug=True)