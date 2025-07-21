# 🛡️ Sistema de Detecção de Ameaças Cibernéticas

Este é um projeto Flask com foco em **segurança digital**, que permite:

- 📁 Analisar arquivos `.txt` ou `.log` para detectar padrões de atividades maliciosas
- 🔗 Verificar a reputação de links suspeitos através da API IPQualityScore
- 🖼️ Interface visual personalizada 
- 🌐 Deploy em produção usando Render + Uptime Robot

---

## 🚀 Tecnologias Utilizadas

- python
- Html e CSS
- **Flask** — Framework web em Python
- **Jinja2** — Templates HTML dinâmicos
- **Chardet** — Detecta codificação de arquivos `.txt` ou `.log`
- **Requests** — Consome APIs externas
- **Gunicorn** — Servidor WSGI para produção
- **Render** — Hospedagem do projeto
- **Uptime Robot** — Monitoramento contínuo para manter a aplicação disponível 24h


---

## 🧰 Funcionalidades :

### 📁 Análise de arquivos de texto

- Detecta comandos suspeitos como:
  - `DROP TABLE`, `exec("/bin/bash")`, `<script>`, `Failed password`
  - Ataques de SQL Injection ou tentativas de invasão

### 🔗 Verificação de links

- Utiliza a [API IPQualityScore](https://ipqualityscore.com/documentation/url-scanner)
- Retorna nível de risco, comportamento malicioso ou phishing

---

## 📂 Estrutura do Projeto
ne

ids-rules/
├── app.py               # Executa o servidor
├── rules.py             # Regras de detecção
├── templates/
│   └── index.html       # Página HTML
├── static/
│   └── style.css        # Estilo dark
└── README.md            # Este documento 

---

## Projeto voltado para pessoas comuns
Este IDS foi criado pensando não apenas em desenvolvedores, mas também em **usuários não técnicos**, ou seja, pessoas comuns que desejam monitorar atividades suspeitas mas **não sabem programar** ou instalar nada complicado, tornando assim este projeto realmente funcional e importante.
Basta acessar o sistema via navegador — sem necessidade de baixar Python, mexer com terminal ou configurar ambiente. O projeto roda online com visual dark mode e já exibe os logs e alertas automaticamente.

---

## requirements.txt
Este arquivo contém as **bibliotecas necessárias** para que o projeto funcione corretamente quando instalado em ambientes de deploy (como servidores online ou ambientes virtuais):

---

## 👩‍💻 Autoria
Projeto desenvolvido por **Julianna**, durante estudos sobre programação , cibersegurança e monitoramento de sistemas.
