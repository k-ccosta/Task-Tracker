def exibir_titulo():
    print("""
            Task Tracker
        """)

def exibir_menu():
    menu_opcoes = ["Adicionar Tarefa", "Atualizar Tarefa", "Excluir Tarefa"]

    for indice, opcao in enumerate(menu_opcoes):
        print(f"[{indice}] - {opcao}")

if __name__ == "__main__":
    exibir_titulo()
    exibir_menu()