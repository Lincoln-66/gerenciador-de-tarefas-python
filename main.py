def cadastrar_tarefas(tarefas):
    n = 0 

    qntTarefas = int(input("Quantas tarefas deseja cadastrar? "))

    while n < qntTarefas :
        nome = input("Nome da tarefa: ")
                
        tarefa = {
        "nome": nome,
        "concluida": False }

        tarefas.append(tarefa)
        n+=1

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Sem tarefas")
        return

    print("---Tarefas---")
    
    for i, tarefa in enumerate(tarefas,start= 0):
        if tarefa["concluida"]:
            estado = "Concluida"
        else:
            estado = "Pendente"

        print(f'{i+1}. {tarefa['nome']} -- {estado}')

def concluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Sem Tarefas Registradas\n")
    elif len(tarefas)> 0:
        print("--- CONCLUIR TAREFAS ---")
    for i in range(len(tarefas)):
        if tarefas[i]["concluida"] == False:
            print(f"{i+1}. {tarefas[i]['nome']} -- Pendente")
            

            
    concluir = int(input("Qual tarefa voce quer marcar? \n"))
 
    tarefas[concluir - 1]["concluida"] = True


    if len(tarefas) == 0:
        print("voce terminou todas as suas atividades!!\n")

    for i in range(len(tarefas)):
        if tarefas[i]["concluida"] == False:
            print(f"\n{i+1}. {tarefas[i]['nome']} -- Pendente")
    else:
        print(f"\n{i+1}. {tarefas[i]['nome']} -- Concluida")

def excluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("Sem Tarefas Registradas\n")
    elif len(tarefas) > 0:
        print("---Deletar tarefa---")
        deletar = int(input("Deletar: "))
        tarefas.pop(deletar - 1)
                    
tarefas = []






while True:
    n = 0
    print("\n-----MENU-----")
    print("1. Cadastar tarefa\n" \
        "2. Lista tarefas\n"
        "3. Concluir tarefa\n"\
        "4. Excluir\n"
        "0. Sair\n")
     
    opcao = int(input())
    match opcao:
        case 0:
            break
        case 1:
            cadastrar_tarefas(tarefas)
            print("\n")        
        case 2:
            listar_tarefas(tarefas)
            print("\n")
        case 3:
            concluir_tarefa(tarefas)
            print("\n")
        case 4:
            excluir_tarefa(tarefas)
            print("\n")