from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", alerts=None)

@app.route("/upload", methods=["POST"])
def upload_log():
    file = request.files["logfile"]
    content = file.read().decode("utf-8")
    logs = content.splitlines()
    
    alerts = detect_suspicious_activity(logs)  # sua função de análise
    return render_template("index.html", alerts=alerts)