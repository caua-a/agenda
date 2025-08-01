lista_tarefas=[]
lista_concluido=[]
def Adicionar_tarefa():
    tarefa=input("Qual a sua tarefa?  ").lower()
    if tarefa not in lista_tarefas:
        lista_tarefas.append(tarefa)
        print(f"{tarefa} foi adicionado a sua agenda.")
    else:
        print("Essa tarefa já está na lista.")


def Remover_tarefa():
    while True:
        tarefa_removida= input("Qual a tarefa deseja remover?   ").lower()
        if tarefa_removida not in lista_tarefas:
            
            print("Esta tarefa não existe.")
        else:
            lista_tarefas.remove(tarefa_removida)
            print(f"Sua tarefa '{tarefa_removida}' foi removida com sucesso.")
            break



def Listar():
    if len(lista_tarefas)== 0:
        print("Sua lista está vazia")
    else:
        for x in lista_tarefas:
            print(f'[ ] {x}')


def Sair():
    print("Obrigado por usar nossos serviços!")
    quit()

def concluida():
    
    while True:
        concluir=input("Qual tarefa a ser concluída? ")
        if concluir not in lista_tarefas:
            print("Esta tarefa não existe.")

        else:
            lista_tarefas.remove(concluir)
            lista_concluido.append(concluir)
            print(f"Sua tarefa {concluir} foi concluída.")
            break
            

def listar_concluidos():
    for x in lista_concluido:
            print(f"[x] {x}")