lista = []
concluidos = []

def ver_tarefas():
    print("==================================== TAREFAS ====================================")
    for i in range(0, len(lista)):
        print(i+1, "-", lista[i])
                
def adicionar(): 
    tarefa = input("Qual nome da tarefa:")
    lista.append(tarefa)

def concluido():
    valor_tarefa = int(input("Digite o valor da tarefa conlcuida:"))
    if valor_tarefa > len(lista):
        print("Valor inválido tente novamente!")
    else:
        concluidos.append(lista[valor_tarefa-1])
        lista.pop(valor_tarefa-1)

while True:
    print("======================================= SUAS TAREFAS =======================================\n")
    for i in range(0, len(lista)):
        print(i+1, "-", lista[i])
    print("\n======================================= REALIZADAS =========================================\n")
    for i in range(0, len(concluidos)):
        print(i+1, "-", concluidos[i]) 
    print("\n============================================================================================")
    print("\n > Digite o valor da opção desejada <")
    print("\n1- Adicionar tarefa  \n2- Concluir tarefa \n3- Sair")   
    acao = int(input("\n\n>"))

    match acao: 
        case 1:
            adicionar()
        case 2:
            if len(lista) > 0:
                concluido()
        case 3:
            break