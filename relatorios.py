import json
import os

arquivoUsuarios = "usuarios.json"
arquivoHabitos = "habitos.json"
arquivoRegistros = "registros.json"

def carregar_json(arquivo):
    if not os.path.exists(arquivo) or os.path.getsize(arquivo) == 0:
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def relatorio_simples():
    usuarios = carregar_json(arquivoUsuarios)
    habitos = carregar_json(arquivoHabitos)
    registros = carregar_json(arquivoRegistros)

    if not usuarios:
        print("\nNenhum usuário cadastrado.\n")
        return

    if not habitos:
        print("\nNenhum hábito cadastrado.\n")
        return

    if not registros:
        print("\nNenhum registro cadastrado.\n")
        return

    print("\n--- Usuários ---")
    for u in usuarios:
        print(f"ID: {u['id']} - Nome: {u['nome']}")

    try:
        uid = int(input("\nDigite o ID do usuário: "))
    except:
        print("\nID inválido.\n")
        return

    usuario = next((u for u in usuarios if u["id"] == uid), None)
    if not usuario:
        print("\nUsuário não encontrado.\n")
        return

    habitos_usuario = [h for h in habitos if h["usuario_id"] == uid]
    if not habitos_usuario:
        print("\nEste usuário não tem hábitos cadastrados.\n")
        return

    print("\n--- Hábitos do usuário ---")
    for h in habitos_usuario:
        print(f"ID: {h['id']} - {h['titulo']} (Meta: {h['meta']})")

    try:
        hid = int(input("\nDigite o ID do hábito: "))
    except:
        print("\nID inválido.\n")
        return

    habito = next((h for h in habitos_usuario if h["id"] == hid), None)
    if not habito:
        print("\nHábito não encontrado.\n")
        return

    registros_habito = [r for r in registros if r["habito_id"] == hid]
    if not registros_habito:
        print("\nNenhum registro para esse hábito.\n")
        return

    total = len(registros_habito)
    meta = habito["meta"]
    atingidos = sum(1 for r in registros_habito if r["valor"] >= meta)
    porcentagem = (atingidos / total) * 100

    print("\n===== Relatório Simples =====")
    print(f"Usuário: {usuario['nome']}")
    print(f"Hábito: {habito['titulo']}")
    print(f"Meta diária: {meta}")
    print(f"Total de registros: {total}")
    print(f"Dias que bateram a meta: {atingidos}")
    print(f"Percentual de dias com meta atingida: {porcentagem:.1f}%")
    print("=============================\n")


def relatorios():
    while True:
        print("""
--- Menu de Relatórios ---
1 - Relatório simples por hábito
2 - Voltar
""")
        op = input("Escolha sua opção: ")

        if op == "1":
            relatorio_simples()
        elif op == "2":
            break
        else:
            print("\nOpção inválida!\n")
