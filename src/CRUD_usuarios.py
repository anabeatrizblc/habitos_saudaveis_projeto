import json
import os
from datetime import datetime

arquivoUsuarios = "data/usuarios.json"

def carregar():
    if not os.path.exists(arquivoUsuarios) or os.path.getsize(arquivoUsuarios) == 0:
        return []
    with open(arquivoUsuarios, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar(dados):
    with open(arquivoUsuarios, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def calcular_idade(data_nascimento):
    try:
        nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    except:
        return "Data inválida"
    hoje = datetime.now()
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade

def criar_usuario():
    print("\n--- Criar novo usuário ---")
    nome = input("Nome do usuário: ").strip().capitalize()
    email = input("Email do usuário: ").strip().lower()
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    data_nasc = input("Data de nascimento (AAAA-MM-DD): ")

    usuarios = carregar()

    if usuarios:
        novo_id = max([u["id"] for u in usuarios]) + 1
    else:
        novo_id = 1

    usuario = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "peso": peso,
        "altura": altura,
        "data_nascimento": data_nasc
    }

    usuarios.append(usuario)
    salvar(usuarios)

    print("\n---> Usuário criado com sucesso! <---\n")

def listar_usuarios():
    usuarios = carregar()

    if not usuarios:
        print("\n/////////////// ERRO: Nenhum usuário cadastrado. ///////////////\n")
        return

    print("\n========== Lista de Usuários ==========\n")

    for u in usuarios:
        idade = calcular_idade(u["data_nascimento"])
        print(f"""
ID: {u['id']}
Nome: {u['nome']}
Email: {u['email']}
Peso: {u['peso']} kg
Altura: {u['altura']} m
Data de Nascimento: {u['data_nascimento']}
Idade: {idade} anos
----------------------------------------------
""")

def atualizar_usuario():
    usuarios = carregar()

    if not usuarios:
        print("\n/////////////// ERRO: Nenhum usuário cadastrado. ///////////////\n")
        return

    listar_usuarios()

    try:
        uid = int(input("Insira o ID do usuário que deseja atualizar: "))
    except:
        print("\nID inválido.\n")
        return

    usuario = next((u for u in usuarios if u["id"] == uid), None)

    if not usuario:
        print("\n/////////////// ERRO: Usuário não encontrado. ///////////////\n")
        return

    print("""
O que deseja atualizar?
1 - Nome
2 - Email
3 - Peso
4 - Altura
5 - Data de nascimento
""")

    op = input("Escolha sua opção: ")

    if op == "1":
        usuario["nome"] = input("Novo nome: ").capitalize()
    elif op == "2":
        usuario["email"] = input("Novo email: ").lower()
    elif op == "3":
        usuario["peso"] = float(input("Novo peso (kg): "))
    elif op == "4":
        usuario["altura"] = float(input("Nova altura (m): "))
    elif op == "5":
        usuario["data_nascimento"] = input("Nova data (AAAA-MM-DD): ")
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
        uid = int(input("Insira o ID do usuário que deseja deletar: "))
    except:
        print("\nID inválido.\n")
        return

    usuario = next((u for u in usuarios if u["id"] == uid), None)

    if not usuario:
        print("\n/////////////// ERRO: Usuário não encontrado. ///////////////\n")
        return

    confirmar = input("Tem certeza que deseja deletar? ('Sim'/'Não'): ")

    if confirmar.lower() != "sim":
        return

    usuarios = [u for u in usuarios if u["id"] != uid]
    salvar(usuarios)

    print("\nUsuário deletado com sucesso!\n")

def usuarios():
    while True:
        print("""
1 - Criar usuário
2 - Listar usuários
3 - Atualizar usuário
4 - Deletar usuário
5 - Voltar
""")

        op = input("Escolha sua opção: ")

        if op == "1":
            criar_usuario()
        elif op == "2":
            listar_usuarios()
        elif op == "3":
            atualizar_usuario()
        elif op == "4":
            deletar_usuario()
        elif op == "5":
            break
        else:
            print("\nOpção inválida!\n")

