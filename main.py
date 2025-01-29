import os
from datetime import datetime

task_list = []

def inicializar_tracker():
    exibir_titulo()
    menu_opcoes = exibir_menu()
    selecionar_menu(menu_opcoes)
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

def adicionar_tarefa():
    task = {
        "id":len(task_list) + 1,
        "description":input("Digite uma descrição: "),
        "status":"to-do",
        "createdAt":datetime.now(),
        "updatedAt":datetime.now()        
    }    

    task_list.append(task)
    print("\nTarefa adicionada com sucesso!\n")

    resposta = input("Deseja adicionar mais alguma tarefa? \n[S]/[N]: ").upper().strip()

    if resposta == "S":
        limpar_tela()
        adicionar_tarefa()
    else:
        limpar_tela()
        inicializar_tracker()

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

    if indice_selecionado == 0:
        limpar_tela()
        adicionar_tarefa()

if __name__ == "__main__":
    inicializar_tracker()