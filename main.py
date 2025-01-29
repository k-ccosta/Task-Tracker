import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")  
def exibir_titulo():
    print("""
            Task Tracker
        """)
def exibir_menu():
    menu_opcoes = ["Adicionar Tarefa", "Atualizar Tarefa", "Excluir Tarefa"]

    for indice, opcao in enumerate(menu_opcoes):
        print(f"[{indice}] - {opcao}")

    return menu_opcoes

def selecionar_menu(menu_opcoes):
    while True:
        try:
            indice_selecionado = int(input("\nO que você deseja fazer? "))
            
            if indice_selecionado in range(len(menu_opcoes)):
                break
            else:
                print(f"OPÇÃO INVÁLIDA! Por favor, selecione uma opção entre 0 e {len(menu_opcoes)-1}")                
        except ValueError:
            print("OPÇÃO INVÁLIDA! Por favor, informe um número inteiro.")


if __name__ == "__main__":
    exibir_titulo()
    menu_opcoes = exibir_menu()
    selecionar_menu(menu_opcoes)