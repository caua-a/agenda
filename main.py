from func import Adicionar_tarefa, Remover_tarefa, Sair, concluida, carregar_tarefas, lista_tarefas
opcoes=[]
while True:
    print('''
        ╔════════════════════════════════════════════════════════╗
        ║                TO-DO LIST - MENU PRINCIPAL             ║
        ╠════════════════════════════════════════════════════════╣
        ║  1. Adicionar Tarefa                                   ║
        ║  2. Remover Tarefa                                     ║
        ║  3. Listar Tarefas                                     ║
        ║  4. Concluir                                           ║
        ║  0. Sair                                               ║
        ╠════════════════════════════════════════════════════════╣
            '''
    )
    escolha=(input("     Escolha uma opção e pressione Enter:"))
    opcoes.append(escolha)
    if escolha == "1":
        Adicionar_tarefa()

    elif escolha == "2":
        if len(lista_tarefas) == 0:
            print("Não tem nenhuma tarefa.")
        else:
            Remover_tarefa()

    elif escolha == "3":
        carregar_tarefas("tarefas.txt")
        if lista_tarefas:
            print("tarefas pendentes")
            for i, tarefa in enumerate(lista_tarefas, 1):
                print(f"{i}. {tarefa}")
        else:
            print("Nenhuma tarefa encontrada.")

    
    elif escolha == '4':
        concluida()
        carregar_tarefas("concluidas.txt", lista_tarefas)
    
    elif escolha == '0':
        Sair()
    
    else:
        print("Digite uma opção válida.")





