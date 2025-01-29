import os
from datetime import datetime

task_list = []

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")  

def exibir_titulo():
    print("""
            Task Tracker
        """)

def exibir_menu():
    menu_opcoes = ["Adicionar Tarefa", "Atualizar Tarefa", "Excluir Tarefa", "Sair"]
    for indice, opcao in enumerate(menu_opcoes):
        print(f"[{indice}] - {opcao}")
    return menu_opcoes

def adicionar_tarefa():
    while True:
        task = {
            "id": len(task_list) + 1,  # Gera um ID único
            "description": input("Digite uma descrição: "),
            "status": "to-do",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        task_list.append(task)
        print("Tarefa adicionada com sucesso!")

        # Pergunta se o usuário deseja adicionar mais tarefas
        resposta = input("Deseja adicionar mais alguma tarefa? [S]/[N]: ").strip().lower()
        if resposta != "s":
            limpar_tela()
            break  # Sai do loop e retorna ao menu principal

def selecionar_menu(menu_opcoes):
    while True:
        try:
            indice_selecionado = int(input("\nO que você deseja fazer? "))
            
            if indice_selecionado in range(len(menu_opcoes)):
                return indice_selecionado  # Retorna a escolha do usuário
            else:
                print(f"OPÇÃO INVÁLIDA! Por favor, selecione uma opção entre 0 e {len(menu_opcoes)-1}")                
        except ValueError:
            print("OPÇÃO INVÁLIDA! Por favor, informe um número inteiro.")

if __name__ == "__main__":
    while True:
        limpar_tela()
        exibir_titulo()
        menu_opcoes = exibir_menu()
        opcao = selecionar_menu(menu_opcoes)

        if opcao == 0:  # Adicionar Tarefa
            limpar_tela()
            adicionar_tarefa()
        elif opcao == 1:  # Atualizar Tarefa
            limpar_tela()
            print("Funcionalidade de atualizar tarefa ainda não implementada.")
        elif opcao == 2:  # Excluir Tarefa
            limpar_tela()
            print("Funcionalidade de excluir tarefa ainda não implementada.")
        elif opcao == 3:  # Sair
            limpar_tela()
            print("Saindo do Task Tracker. Até logo!")
            break
