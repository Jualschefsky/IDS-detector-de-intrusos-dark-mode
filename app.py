from flask import Flask, request, render_template
import chardet
import requests
import urllib.parse  # ✅ Para codificar o link corretamente

app = Flask(__name__)

IPQS_API_KEY = "ODJwYMfNHOXifP5bL6RyIukyu63ZWWX"  # 🔐 Sua chave da API

# 📁 Função para ler e decodificar arquivos .txt ou .log
def ler_arquivo_texto(file):
    raw_data = file.read()
    resultado = chardet.detect(raw_data)
    codificacao = resultado['encoding'] if resultado['encoding'] else 'utf-8'

    try:
        texto = raw_data.decode(codificacao)
        return texto
    except Exception:
        return "⚠️ Não foi possível decodificar o conteúdo do arquivo."

# 🚨 Função para detectar padrões suspeitos
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

# 🔗 Verificação de reputação do link
def analisar_link(link):
    link_codificado = urllib.parse.quote(link, safe='')  # ✅ Codifica caracteres especiais
    url = f"https://ipqualityscore.com/api/json/url/{IPQS_API_KEY}/{link_codificado}"

    try:
        resposta = requests.get(url)

        if resposta.headers.get("Content-Type", "").startswith("application/json"):
            dados = resposta.json()
            risco = dados.get("risk_score", 0)

            # Estilo baseado em níveis de risco
            if dados.get("malicious") or risco >= 70:
                return f"⚠️ Atenção: Este link apresenta risco elevado!\nNível de ameaça: {risco}%"
            elif risco >= 40:
                return f"⚠️ Possível comportamento suspeito detectado.\nRisco moderado: {risco}%"
            else:
                return f"🛡️ Nenhuma ameaça detectada. Link parece seguro.\nRisco: {risco}%"
        else:
            return "⚠️ Erro: a resposta da API não está em formato JSON."
    except Exception as e:
        return f"⚠️ Erro ao analisar o link: {str(e)}"

# 🌐 Rota principal da aplicação
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ""
    resultado_link = ""

    if request.method == 'POST':
        arquivo = request.files.get('file')
        link = request.form.get('link')

        # 📁 Análise de arquivo enviado
        if arquivo and arquivo.filename.endswith(('.txt', '.log')):
            conteudo = ler_arquivo_texto(arquivo)
            resultado = detect_suspicious_activity(conteudo)
        elif arquivo:
            resultado = "⚠️ Tipo de arquivo não suportado para análise."

        # 🔗 Análise de link digitado
        if link:
            resultado_link = analisar_link(link)

    return render_template('index.html', resultado=resultado, resultado_link=resultado_link)

# 🚀 Inicializa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)