lista_tarefas=[]
lista_concluido=[]
import json
f= open("tarefas.txt")

lista_tarefas = []
lista_concluido = []

def Adicionar_tarefa():
    tarefa = input("Qual a sua tarefa?  ").lower()
    if tarefa not in lista_tarefas:
        lista_tarefas.append(tarefa)
        print(f"{tarefa} foi adicionado a sua agenda.")
        with open("tarefas.txt", "a", encoding="utf-8") as f:
            f.write(tarefa + "\n")
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
            salvar_tarefas("tarefas.txt", lista_tarefas)
            break



def carregar_tarefas(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for x in f:
                tarefa = x.strip("\n")
                if tarefa not in lista_tarefas:
                    lista_tarefas.append(tarefa)
    except FileNotFoundError:
        pass



def salvar_tarefas(nome_arquivo, lista):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for tarefa in lista:
            f.write(tarefa + "\n")



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






def ler_lista():
    pass