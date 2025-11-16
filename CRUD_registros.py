import json
import os
from datetime import date

arquivoRegistros = "registros.json"
arquivoUsuarios = "usuarios.json"
arquivoHabitos = "habitos.json"

def carregar_registros():
    if not os.path.exists(arquivoRegistros) or os.path.getsize(arquivoRegistros) == 0:
        return []
    return json.load(open(arquivoRegistros, "r", encoding="utf-8"))

def salvar_registros(dados):
    with open(arquivoRegistros, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_usuarios():
    if not os.path.exists(arquivoUsuarios) or os.path.getsize(arquivoUsuarios) == 0:
        return []
    return json.load(open(arquivoUsuarios, "r", encoding="utf-8"))

def carregar_habitos():
    if not os.path.exists(arquivoHabitos) or os.path.getsize(arquivoHabitos) == 0:
        return []
    return json.load(open(arquivoHabitos, "r", encoding="utf-8"))

def criar_registro():
    print("\n--- Criar registro diário ---")

    usuarios = carregar_usuarios()
    if not usuarios:
        print("\nNenhum usuário cadastrado.\n")
        return

    print("\n--- Usuários ---")
    for u in usuarios:
        print(f"ID: {u['id']} - Nome: {u['nome']}")

    uid = int(input("Insira o ID do usuário: "))

    habitos = carregar_habitos()
    habitos_usuario = [h for h in habitos if h["usuario_id"] == uid]

    if not habitos_usuario:
        print("\nEsse usuário não possui hábitos cadastrados.\n")
        return

    print("\n--- Hábitos do usuário ---")
    for h in habitos_usuario:
        print(f"ID: {h['id']} - Título: {h['titulo']}")

    hid = int(input("Insira o ID do hábito: "))

    valor = float(input("Insira o valor do registro (ex: quantidade): "))
    obs = input("Observação (opcional): ") or "Sem observação"
    data_reg = input("Data (YYYY-MM-DD) ou Enter para hoje: ")

    if data_reg.strip() == "":
        data_reg = date.today().isoformat()

    registros = carregar_registros()

    if registros:
        novo_id = max([r["id"] for r in registros]) + 1
    else:
        novo_id = 1

    registro = {
        "id": novo_id,
        "usuario_id": uid,
        "habito_id": hid,
        "data": data_reg,
        "valor": valor,
        "observacao": obs
    }

    registros.append(registro)
    salvar_registros(registros)

    print("\n---> Registro criado com sucesso! <---\n")

def listar_registros():
    registros = carregar_registros()

    if not registros:
        print("\nNenhum registro cadastrado.\n")
        return

    print("\n--- Lista de Registros ---\n")
    for r in registros:
        print(f"ID: {r['id']} | Usuário: {r['usuario_id']} | Hábito: {r['habito_id']} | Data: {r['data']} | Valor: {r['valor']} | Obs: {r['observacao']}")

def atualizar_registro():
    registros = carregar_registros()

    if not registros:
        print("\nNenhum registro cadastrado.\n")
        return

    listar_registros()

    rid = int(input("\nInsira o ID do registro: "))

    registro = next((r for r in registros if r["id"] == rid), None)

    if not registro:
        print("\nRegistro não encontrado.\n")
        return

    print("\n1- Alterar valor\n2- Alterar observação\n3- Alterar data")
    opcao = input("Escolha sua opção: ")

    if opcao == "1":
        registro["valor"] = float(input("Novo valor: "))
    elif opcao == "2":
        registro["observacao"] = input("Nova observação: ")
    elif opcao == "3":
        registro["data"] = input("Nova data (YYYY-MM-DD): ")
    else:
        print("\nOpção inválida.\n")
        return

    salvar_registros(registros)
    print("\nRegistro atualizado com sucesso!\n")
