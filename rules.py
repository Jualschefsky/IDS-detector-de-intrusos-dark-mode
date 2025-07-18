def detect_suspicious_activity(logs):
    alerts = []

    for i, line in enumerate(logs):
        # Detecta 5 falhas de login em sequência
        if "falha_login" in line:
            count = sum(1 for l in logs[i:i+5] if "falha_login" in l)
            if count >= 5:
                alerts.append(f"[ALERTA] Múltiplas falhas de login na linha {i}.")

        # Detecta acessos restritos às 23h
        if "acesso_restrito" in line and "hora=23" in line:
            alerts.append(f"[ALERTA] Acesso restrito fora do horário - linha {i}.")

    return alerts