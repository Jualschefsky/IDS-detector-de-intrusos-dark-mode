from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", alerts=None)

@app.route("/upload", methods=["POST"])
def upload_log():
    # Proteção contra ausência de arquivo
    if "logfile" not in request.files:
        return "❌ Nenhum arquivo foi enviado. Por favor selecione um arquivo .txt.", 400

    file = request.files["logfile"]

    # Proteção contra arquivo vazio
    if file.filename == "":
        return "❌ Arquivo vazio. Selecione um arquivo válido.", 400

    try:
        content = file.read().decode("utf-8")
        logs = content.splitlines()

        # Função de detecção personalizada (você pode adaptar a lógica)
        alerts = detect_suspicious_activity(logs)

        return render_template("index.html", alerts=alerts)

    except Exception as e:
        return f"❌ Erro ao processar o arquivo: {str(e)}", 500