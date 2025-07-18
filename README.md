# 🔐 IDS - Sistema de Detecção de Intrusos

Este projeto simula um sistema IDS baseado em regras simples escritas em Python. Ele analisa registros de log e exibe alertas de segurança em uma interface web criada com Flask.

---

## 🚨 Funcionalidades

- Detecta múltiplas falhas de login consecutivas
- Identifica acessos restritos fora do horário permitido
- Exibe os alertas e os logs analisados via navegador

---

## 🛠️ Tecnologias

- Python
- Flask
- HTML + CSS
- Jinja2 (template engine)

---

## 💻 Interface do Sistema

![Interface IDS](interface.png)

---

## 📦 Estrutura do Projeto

ids-rules/
├── app.py               # Executa o servidor
├── rules.py             # Regras de detecção
├── logs.txt             # Logs simulados
├── templates/
│   └── index.html       # Página HTML
├── static/
│   └── style.css        # Estilo dark
└── README.md            # Este documento 

---

## Projeto voltado para pessoas comuns
Este IDS foi criado pensando em **usuários não técnicos**, ou seja, pessoas comuns que desejam monitorar atividades suspeitas mas **não sabem programar** ou instalar nada complicado.

Basta acessar o sistema via navegador — sem necessidade de baixar Python, mexer com terminal ou configurar ambiente. O projeto roda online com visual dark mode e já exibe os logs e alertas automaticamente.

---

## requirements.txt
Este arquivo contém as **bibliotecas necessárias** para que o projeto funcione corretamente quando instalado em ambientes de deploy (como servidores online ou ambientes virtuais):

---

## 👩‍💻 Autoria
Projeto desenvolvido por **Julianna**, durante estudos sobre programação , cibersegurança e monitoramento de sistemas.
