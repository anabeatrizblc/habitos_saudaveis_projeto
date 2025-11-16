from CRUD_usuarios import usuarios
from CRUD_habitos import habitos
from CRUD_registros import registros

def menu_principal():
    print("\033[1;36m")
    print("\n============ Sistema de Hábitos Saudáveis ============")
    print("1 - Usuários")
    print("2 - Hábitos")
    print("3 - Registros Diários")
    print("4 - Sair")
    print("======================================================")
    print("\033[0m")

def app():
    while True:
        menu_principal()
        opcao = input("Escolha sua opção: ")

        if opcao == "1":
            usuarios()

        elif opcao == "2":
            habitos()

        elif opcao == "3":
            registros()

        elif opcao == "4":
            print("\nSaindo do sistema... Até logo!\n")
            break
        
        else:
            print("\n/////////////// ERRO: Opção inválida! ///////////////\n")

if __name__ == "__main__":
    app()
