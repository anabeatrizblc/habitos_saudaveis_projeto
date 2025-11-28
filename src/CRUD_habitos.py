import json
import os

arquivoUsuarios = "data/usuarios.json"
arquivoHabitos = "data/habitos.json"


def carregar_usuarios():
    if not os.path.exists(arquivoUsuarios) or os.path.getsize(arquivoUsuarios) == 0:
        return []
    with open(arquivoUsuarios, "r", encoding="utf-8") as f:
        return json.load(f)


def carregar_habitos():
    if not os.path.exists(arquivoHabitos) or os.path.getsize(arquivoHabitos) == 0:
        return []
    with open(arquivoHabitos, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_habitos(dados):
    with open(arquivoHabitos, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def criar_habito():
    print("\n--- Criar novo hábito ---")

    usuarios = carregar_usuarios()
    if not usuarios:
        print("\nNenhum usuário cadastrado. Cadastre um usuário primeiro.\n")
        return

    print("\nUsuários cadastrados:")
    for u in usuarios:
        print(f"ID: {u['id']} - Nome: {u['nome']}")

    try:
        usuario_id = int(input("\nDigite o ID do usuário dono do hábito: "))
    except:
        print("\nID inválido.\n")
        return

    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        print("\nUsuário não encontrado.\n")
        return

    titulo = input("Título do hábito (ex: Beber água): ").strip()
    try:
        meta = float(input("Meta diária (ex: 2 para 2 litros, 8000 para passos): "))
    except:
        print("\nValor inválido para meta.\n")
        return

    habitos = carregar_habitos()
    if habitos:
        novo_id = max(h["id"] for h in habitos) + 1
    else:
        novo_id = 1

    habito = {
        "id": novo_id,
        "usuario_id": usuario_id,
        "titulo": titulo,
        "meta": meta
    }

    habitos.append(habito)
    salvar_habitos(habitos)

    print("\nHábito criado com sucesso!\n")


def listar_habitos():
    habitos = carregar_habitos()
    if not habitos:
        print("\nNenhum hábito cadastrado.\n")
        return

    print("\n========== Lista de Hábitos ==========\n")
    for h in habitos:
        print(f"ID: {h['id']} | Usuário ID: {h['usuario_id']} | Título: {h['titulo']} | Meta: {h['meta']}")
    print()


def atualizar_habito():
    habitos = carregar_habitos()
    if not habitos:
        print("\nNenhum hábito cadastrado.\n")
        return

    listar_habitos()

    try:
        hid = int(input("Digite o ID do hábito que deseja atualizar: "))
    except:
        print("\nID inválido.\n")
        return

    habito = next((h for h in habitos if h["id"] == hid), None)
    if not habito:
        print("\nHábito não encontrado.\n")
        return

    print("""
O que deseja atualizar?
1 - Título
2 - Meta diária
""")
    op = input("Escolha sua opção: ")

    if op == "1":
        habito["titulo"] = input("Novo título: ").strip()
    elif op == "2":
        try:
            habito["meta"] = float(input("Nova meta diária: "))
        except:
            print("\nValor inválido.\n")
            return
    else:
        print("\nOpção inválida.\n")
        return

    salvar_habitos(habitos)
    print("\nHábito atualizado com sucesso!\n")


def deletar_habito():
    habitos = carregar_habitos()
    if not habitos:
        print("\nNenhum hábito cadastrado.\n")
        return

    listar_habitos()

    try:
        hid = int(input("Digite o ID do hábito que deseja deletar: "))
    except:
        print("\nID inválido.\n")
        return

    habito = next((h for h in habitos if h["id"] == hid), None)
    if not habito:
        print("\nHábito não encontrado.\n")
        return

    habitos = [h for h in habitos if h["id"] != hid]
    salvar_habitos(habitos)

    print("\nHábito deletado com sucesso!\n")


def habitos():
    while True:
        print("""
--- Menu de Hábitos ---
1 - Criar hábito
2 - Listar hábitos
3 - Atualizar hábito
4 - Deletar hábito
5 - Voltar
""")

        op = input("Escolha sua opção: ")

        if op == "1":
            criar_habito()
        elif op == "2":
            listar_habitos()
        elif op == "3":
            atualizar_habito()
        elif op == "4":
            deletar_habito()
        elif op == "5":
            break
        else:
            print("\nOpção inválida!\n")
