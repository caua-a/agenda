from func import Adicionar_tarefa
from func import Remover_tarefa
from func import Listar
from func import Sair
from func import concluida
from func import listar_concluidos
from func import salvar_tarefas
from func import carregar_tarefas
from func import lista_tarefas
from func import ler_lista
import time
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
        ║  5. Listar Concluídos                                  ║
        ║  6. Sair                                               ║
        ╠════════════════════════════════════════════════════════╣
            '''
    )
    escolha=(input("     Escolha uma opção e pressione Enter:"))
    opcoes.append(escolha)
    if escolha == "1":
        Adicionar_tarefa()
        # não precisa chamar salvar_tarefas aqui, pois já salva na função

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
            time.sleep(5)
        else:
            print("Nenhuma tarefa encontrada.")

    
    elif escolha == '4':
        concluida()
        carregar_tarefas("concluidas.txt", lista_tarefas)
        # time.sleep(5)
    
    elif escolha == '5':
        listar_concluidos()
    
    elif escolha == '6':
        Sair()
    
    else:
        print("Digite uma opção válida.")
        # time.sleep(2)





