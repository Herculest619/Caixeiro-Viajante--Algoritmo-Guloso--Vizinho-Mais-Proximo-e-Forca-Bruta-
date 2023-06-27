import time
import itertools

def forcaBruta(G):
    inicio = time.time()
    print("Processando . . .")
    cost_min = float("inf")                   #armazena custo minimo
    C_best = None                             #armazena o melhor caminho

    C = list()                                #criando uma lista auxiliar do tamanho de G
    for i in range(len(G)):
        C.append(i)

    perm_iterator = itertools.permutations(C)   #Realiza a permutação da lista

    for C in perm_iterator:                   #Percorre as Listas geradas pela perputação
        C = list(C)                           #Convertendo a tupla em lista
        C.append(C[0])                        #Adicionando o primeiro elemento para fechar o ciclo
        cost_c = 0
        for i in range(len(C)):
            if i+1 < len(C):
                cost_c += G[C[i]][C[i+1]]     #Calcula o custo de cada permutação
        if cost_min > cost_c:
            cost_min = cost_c
            C_best = C
        aux = time.time()

        if aux - inicio >= 600: #Retorna melhor rota em até 10 min
            fim = time.time()
            print("Melhor Rota em ate 10 min:")
            print("Rota: ", C_best)
            print("Custo: ", cost_min)
            print("Tempo:", fim - inicio, "s")
            return fim - inicio

    fim = time.time()
    print("Rota: ", C_best)
    print("Custo: ", cost_min)
    print("Tempo:", fim - inicio, "s")

    return fim - inicio