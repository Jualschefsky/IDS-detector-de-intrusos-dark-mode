# 🛡️ IDS — Detector de Intrusos

Interface web simples e funcional para análise de registros de sistema (.txt) e detecção de comportamentos suspeitos.  
O projeto simula um **Sistema de Detecção de Intrusão (IDS)** básico, ideal para aprender sobre segurança em aplicações web.

## 🚀 Funcionalidades

- Upload de arquivos `.txt` diretamente pela interface
- Análise automática de logs em busca de palavras-chave (como `erro`, `falha`, `suspeito`)
- Geração de relatórios dinâmicos na própria página
- Interface intuitiva e mensagens de alerta em tempo real
- Favicon personalizado e layout responsivo

## 📷 Interface do sistema

![Preview](static/interface-atualizada.png)

## 🧠 Como usar

1. Acesse a aplicação no navegador
2. Envie um arquivo de log (.txt) pelo campo de upload
3. O sistema processa o conteúdo e exibe alertas na tela

---


## 🛠️ Tecnologias

- Python
- Flask
- HTML + CSS
- Hospedagem via render
- UptimeRobot — Monitoramento contínuo da disponibilidade da aplicação online

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
Este IDS foi criado pensando não apenas em desenvolvedores, mas também em **usuários não técnicos**, ou seja, pessoas comuns que desejam monitorar atividades suspeitas mas **não sabem programar** ou instalar nada complicado, tornando assim este projeto realmente funcional e importante.
Basta acessar o sistema via navegador — sem necessidade de baixar Python, mexer com terminal ou configurar ambiente. O projeto roda online com visual dark mode e já exibe os logs e alertas automaticamente.

---

## requirements.txt
Este arquivo contém as **bibliotecas necessárias** para que o projeto funcione corretamente quando instalado em ambientes de deploy (como servidores online ou ambientes virtuais):

---

## 👩‍💻 Autoria
Projeto desenvolvido por **Julianna**, durante estudos sobre programação , cibersegurança e monitoramento de sistemas.
