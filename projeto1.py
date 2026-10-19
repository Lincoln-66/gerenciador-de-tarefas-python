tarefas = []




while True:
    n = 0
    print("\n1. Cadastar tarefa\n" \
        "2. Lista tarefas\n"
        "3. Concluir tarefa\n"\
        "4. Excluir\n"
        "0. Sair\n")
     
    opcao = int(input())
    match opcao:
        case 0:
            break
        case 1:
            qntTarefas = int(input("Quantas tarefas deseja cadastrar? "))

            while n < qntTarefas :
                nome = input("Nome da tarefa: ")
            
                tarefa = {
                "nome": nome,
                "concluida": False
                }

                tarefas.append(tarefa)
                n += 1
            print("\n")        
        case 2:
            print("--- MINHAS TAREFAS ---")
            if len(tarefas) == 0:
                print("Sem Tarefas")

            for i in range(len(tarefas)):
                if tarefas[i]["concluida"] == False:
                    print(f"{i+1}. {tarefas[i]['nome']} -- Pendente")
                else:
                    print(f"{i+1}. {tarefas[i]['nome']} -- Concluida")

            print("\n")

        case 3:
        
            if len(tarefas) == 0:
                print("Sem Tarefas Registradas\n")
            elif len(tarefas)> 0:
                print("--- CONCLUIR TAREFAS ---")
                for i in range(len(tarefas)):
                    if tarefas[i]["concluida"] == False:
                        print(f"{i+1}. {tarefas[i]['nome']} -- Pendente")
                print("\n")
                concluir = int(input("Qual tarefa voce quer marcar? \n"))
 
                tarefas[concluir - 1]["concluida"] = True


                if len(tarefas) == 0:
                    print("voce terminou todas as suas atividades!!\n")

                for i in range(len(tarefas)):
                    if tarefas[i]["concluida"] == False:
                        print(f"\n{i+1}. {tarefas[i]['nome']} -- Pendente")
                    else:
                        print(f"\n{i+1}. {tarefas[i]['nome']} -- Concluida")
        case 4:
            if len(tarefas) == 0:
                print("Sem Tarefas Registradas\n")
            elif len(tarefas) > 0:
                print("---Deletar tarefa---")
                deletar = int(input("Deletar: "))
                tarefas.pop(deletar - 1)
                





        


