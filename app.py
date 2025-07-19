from flask import Flask, render_template, request

app = Flask(__name__)

def detect_suspicious_activity(logs):
    alerts = []
    for line in logs:
        if "erro" in line.lower() or "falha" in line.lower() or "suspeito" in line.lower():
            alerts.append(f"⚠️ Linha suspeita: {line}")
    return alerts

@app.route("/")
def home():
    return render_template("index.html", alerts=None)

@app.route("/upload", methods=["POST"])
def upload_log():
    if "logfile" not in request.files:
        return "❌ Nenhum arquivo enviado.", 400

    file = request.files["logfile"]
    if file.filename == "":
        return "❌ Arquivo vazio. Selecione um válido.", 400

    try:
        content = file.read().decode("utf-8")
        logs = content.splitlines()
        alerts = detect_suspicious_activity(logs)
        return render_template("index.html", alerts=alerts)
    except Exception as e:
        return f"❌ Erro ao processar o arquivo: {str(e)}", 500
        except Exception as e:
        return f"❌ Erro ao processar o arquivo: {str(e)}", 500

     if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

