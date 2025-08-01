from func import Adicionar_tarefa
from func import Remover_tarefa
from func import Listar
from func import Sair
from func import concluida
from func import listar_concluidos
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
        time.sleep(3)
    elif escolha=="2":
        if 1 not in opcoes:
            print("Não tem nenhuma tarefa.")

        else:
            Remover_tarefa()
        time.sleep(3)
    elif escolha=="3":
        Listar()
        time.sleep(5)
    elif escolha == '4':
        concluida()
        time.sleep(5)
    elif escolha == '5':
        listar_concluidos()
    elif escolha == '6':
        Sair()
    else:
        print("Digite uma opção válida.")
        time.sleep(2)





