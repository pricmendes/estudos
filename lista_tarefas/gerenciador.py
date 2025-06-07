def adicionar_tarefa(tarefas, nome_tarefa):
    
    # tarefa: nome da tarefa
    # completada: indica se a tarefa já foi completada ou não
    tarefa = {"nome": nome_tarefa, "completada": False} # false pois sempre iniciará como false
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def visualizar_tarefa(tarefas):
    print("\nLista de tarefas: \n")
    for indice, tarefa in enumerate(tarefas, start = 1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1 # como estamos trabalhando com start=1 precisamos subtrair um número do índice para que não seja feita alteração no índice errado
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}.")
    else:
        print("\n****** Índice de tarefa inválido. ******\n")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["completada"] = True
        print(f"Tarefa {indice_tarefa} marcada como completada.")
    else:
        print("\n****** Índice de tarefa inválido. ******\n")
    return

def deletar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        if tarefas[indice_tarefa_ajustado]["completada"]: # ou pode usar assim if tarefas[indice_tarefa_ajustado]["completada"] == True:
            tarefas.pop(indice_tarefa_ajustado)
            print(f"Tarefa {indice_tarefa} deletada com sucesso!")
        else:
            print("\n****** A tarefa precisa ser completada antes de ser deletada. ******\n")
    else:
        print("\n****** Índice de tarefa inválido. ******\n")
    return        

tarefas = []

while True:
    print("\nMenu Gerenciador da Lista de Tarefas:\n")
    print("1. Adicionar Tarefa.")
    print("2. Ver Tarefas.")
    print("3. Atualizar Tarefa.")
    print("4. Completar Tarefa.")
    print("5. Deletar Tarefas.")
    print("6. Sair.")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        visualizar_tarefa(tarefas)
    
    elif escolha == "3":
        visualizar_tarefa(tarefas)
        indice_tarefa = input("\nDigite o número da tarefa que deseja atualizar: \n")
        novo_nome = input("\nDigite o novo nome da tarefa: \n")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":
        visualizar_tarefa(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
        visualizar_tarefa(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja deletar: ")
        deletar_tarefa(tarefas, indice_tarefa)
        visualizar_tarefa(tarefas)

    elif escolha == "6":
        break
    

print("\nPrograma finalizado.\n")