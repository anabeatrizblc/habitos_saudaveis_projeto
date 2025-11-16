import json
import os

arquivoUsuarios = "usuarios.json"

def carregar():
    if not os.path.exists(arquivoUsuarios) or os.path.getsize(arquivoUsuarios) == 0:
        return []
    with open(arquivoUsuarios, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar(dados):
    with open(arquivoUsuarios, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def criar_usuario():
    print("\n--- Criar novo usuário ---")

    nome = input("Nome do usuário: ").capitalize()
    email = input("Email do usuário: ").lower()

    usuarios = carregar()

    if usuarios:
        novo_id = max([u["id"] for u in usuarios]) + 1
    else:
        novo_id = 1

    usuario = {
        "id": novo_id,
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)
    salvar(usuarios)

    print("\n---> Usuário criado com sucesso! <---\n")

def listar_usuarios():
    usuarios = carregar()

    if not usuarios:
        print("\n/////////////// ERRO: Nenhum usuário cadastrado. ///////////////\n")
        return

    print("\n--- Lista de Usuários ---\n")
    for u in usuarios:
        print(f"ID: {u['id']} - Nome: {u['nome']} - Email: {u['email']}")

def atualizar_usuario():
    usuarios = carregar()

    if not usuarios:
        print("\n/////////////// ERRO: Nenhum usuário cadastrado. ///////////////\n")
        return

    listar_usuarios()

    try:
        uid = int(input("\nInsira o ID do usuário que deseja atualizar: "))
    except:
        print("\nID inválido.\n")
        return

    usuario = next((u for u in usuarios if u["id"] == uid), None)

    if not usuario:
        print("\n/////////////// ERRO: Usuário não encontrado. ///////////////\n")
        return

    print("\n1- Alterar nome\n2- Alterar email")
    opcao = input("Escolha sua opção: ")

    if opcao == "1":
        usuario["nome"] = input("Novo nome: ").capitalize()
    elif opcao == "2":
        usuario["email"] = input("Novo email: ").lower()
    else:
        print("\nOpção inválida.\n")
        return

    salvar(usuarios)
    print("\nUsuário atualizado com sucesso!\n")

def deletar_usuario():
    usuarios = carregar()

    if not usuarios:
        print("\n/////////////// ERRO: Nenhum usuário cadastrado. ///////////////\n")
        return

    listar_usuarios()

    try:
        uid = int(input("\nInsira o ID do usuário que deseja deletar: "))
    except:
        print("\nID inválido.\n")
        return

    usuario = next((u for u in usuarios if u["id"] == uid), None)

    if not usuario:
        print("\n/////////////// ERRO: Usuário não encontrado. ///////////////\n")
        return

    opcao = input("Tem certeza que deseja deletar? ('Sim'/'Não'): ")

    if opcao.lower() != "sim":
        return

    usuarios = [u for u in usuarios if u["id"] != uid]
    salvar(usuarios)

    print("\nUsuário deletado com sucesso!\n")

def usuarios():
    while True:
        print("\n1- Criar usuário\n2- Listar usuários\n3- Atualizar usuário\n4- Deletar usuário\n5- Voltar")
        opcao = input("Escolha sua opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            break
        else:
            print("\nOpção inválida.\n")
