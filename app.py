from flask import Flask, request, render_template
import chardet
import requests
import urllib.parse
import re
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

IPQS_API_KEY =  os.getenv("IPQS_API_KEY")

def ler_arquivo_texto(file):
    raw_data = file.read()
    resultado = chardet.detect(raw_data)
    codificacao = resultado['encoding'] if resultado['encoding'] else 'utf-8'

    try:
        texto = raw_data.decode(codificacao)
        return texto
    except Exception:
        return "⚠️ Não foi possível decodificar o conteúdo do arquivo."

def detect_suspicious_activity(content):
    indicadores = [
        "Failed password", "exec(\"/bin/bash\")", "DROP TABLE", "SELECT * FROM users",
        "Dos attempt", "unauthorized access", "nmap", "alert(", "<script>", "token leak"
    ]
    achados = [termo for termo in indicadores if termo.lower() in content.lower()]

    if achados:
        return f"⚠️ Padrões suspeitos encontrados: {', '.join(achados)}"
    else:
        return "✅ Nenhum comportamento suspeito detectado."

# ✅ Função atualizada: aceita domínios e IPs como válidos
def validar_url(link):
    padrao = re.compile(
        r'^(https?:\/\/)'                         # http:// ou https://
        r'(([\w\-]+\.)+[a-zA-Z]{2,}|'             # domínio com extensão
        r'(\d{1,3}\.){3}\d{1,3})'                 # ou IP (ex: 192.168.0.1)
        r'(\/[^\s]*)?$'                           # caminho opcional
    )
    return bool(padrao.match(link.strip()))

def analisar_link(link):
    if not validar_url(link):
        return "⚠️ Isso não parece um link válido. Digite o endereço completo com http:// ou https://"

    link_formatado = link.strip()
    url = f"https://ipqualityscore.com/api/json/url?key={IPQS_API_KEY}&url={urllib.parse.quote(link_formatado)}&strictness=1"

    try:
        resposta = requests.get(url)
        print("🔎 Conteúdo bruto da resposta:", resposta.text)

        if resposta.headers.get("Content-Type", "").startswith("application/json"):
            dados = resposta.json()
            risco = dados.get("risk_score", 0)
            malicioso = dados.get("malicious", False)
            phishing = dados.get("phishing", False)
            suspicious = dados.get("suspicious", False)

            if malicioso or phishing or suspicious or risco >= 70:
                return f"⚠️ Este link apresenta risco elevado!\nNível de ameaça: {risco}%"
            elif risco >= 40:
                return f"⚠️ Possível comportamento suspeito detectado.\nRisco moderado: {risco}%"
            else:
                return f"🛡️ Nenhuma ameaça detectada. Link parece seguro.\nRisco: {risco}%"
        else:
            return "⚠️ Erro: a resposta da API não está em formato JSON."
    except Exception as e:
        return f"⚠️ Erro ao analisar o link: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ""
    resultado_link = ""

    if request.method == 'POST':
        arquivo = request.files.get('file')
        link = request.form.get('link')

        if arquivo and arquivo.filename.endswith(('.txt', '.log')):
            conteudo = ler_arquivo_texto(arquivo)
            resultado = detect_suspicious_activity(conteudo)
        elif arquivo:
            resultado = "⚠️ Tipo de arquivo não suportado para análise."

        if link:
            resultado_link = analisar_link(link)

    return render_template('index.html', resultado=resultado, resultado_link=resultado_link)

if __name__ == '__main__':
    app.run(debug=True)