import json
import os
from datetime import datetime

arquivoUsuarios = "usuarios.json"
arquivoHabitos = "habitos.json"
arquivoRegistros = "registros.json"

def carregar_json(arquivo):
    if not os.path.exists(arquivo) or os.path.getsize(arquivo) == 0:
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def listar_relatorio():
    usuarios = carregar_json(arquivoUsuarios)
    habitos = carregar_json(arquivoHabitos)
    registros = carregar_json(arquivoRegistros)

    if not usuarios:
        print("\n/////////////// ERRO: Nenhum usuário cadastrado. ///////////////\n")
        return

    if not habitos:
        print("\n/////////////// ERRO: Nenhum hábito cadastrado. ///////////////\n")
        return

    if not registros:
        print("\n/////////////// ERRO: Nenhum registro encontrado. ///////////////\n")
        return

    print("\n--- Usuários ---")
    for u in usuarios:
        print(f"ID: {u['id']} - Nome: {u['nome']}")

    try:
        uid = int(input("\nEscolha o ID do usuário: "))
    except:
        print("\nID inválido.\n")
        return

    usuario = next((u for u in usuarios if u["id"] == uid), None)

    if not usuario:
        print("\n/////////////// ERRO: Usuário não encontrado. ///////////////\n")
        return

    habitos_usuario = [h for h in habitos if h["usuario_id"] == uid]

    if not habitos_usuario:
        print("\n/////////////// ERRO: Este usuário não possui hábitos. ///////////////\n")
        return

    print("\n--- Hábitos ---")
    for h in habitos_usuario:
        print(f"ID: {h['id']} - {h['nome']} (Meta: {h['meta']})")

    try:
        hid = int(input("\nEscolha o ID do hábito: "))
    except:
        print("\nID inválido.\n")
        return

    habito = next((h for h in habitos_usuario if h["id"] == hid), None)

    if not habito:
        print("\n/////////////// ERRO: Hábito não encontrado. ///////////////\n")
        return

    registros_habito = [r for r in registros if r["habito_id"] == hid]

    if not registros_habito:
        print("\n/////////////// ERRO: Nenhum registro deste hábito. ///////////////\n")
        return

    valores = [r["valor"] for r in registros_habito]
    meta = habito["meta"]
    atingidos = sum(1 for r in registros_habito if r["valor"] >= meta)
    nao_atingidos = len(registros_habito) - atingidos
    media = round(sum(valores) / len(valores), 2)
    ultimo = sorted(registros_habito, key=lambda x: x["data"], reverse=True)[0]

    percentual = round((atingidos / len(registros_habito)) * 100, 2)

    print("\n========== Relatório de Progresso ==========\n")
    print(f"Usuário: {usuario['nome']}")
    print(f"Hábito: {habito['nome']}")
    print(f"Meta: {meta}")
    print(f"Total de registros: {len(registros_habito)}")
    print(f"Meta atingida: {atingidos} dias")
    print(f"Meta não atingida: {nao_atingidos} dias")
    print(f"Média dos valores: {media}")
    print(f"Último registro: {ultimo['valor']} em {ultimo['data']}")
    print(f"Progresso geral: {percentual}% de dias com meta atingida")
    print("\n============================================\n")

def relatorios():
    while True:
        print("""
1 - Gerar relatório de evolução
2 - Voltar
""")
        op = input("Escolha sua opção: ")

        if op == "1":
            listar_relatorio()
        elif op == "2":
            break
        else:
            print("\nOpção inválida!\n")
