from flask import Flask, render_template
from rules import detect_suspicious_activity

app = Flask(__name__)

@app.route("/")
def index():
    print("✅ Entrou na rota /")  # ← TESTE: verifica se a função está sendo chamada


    with open("logs.txt") as f:
        logs = f.readlines()
    alerts = []  # TESTE: simula ausência de alertas

    return render_template("index.html", alerts=alerts, logs=logs)

if __name__ == "__main__":
    app.run(debug=True)