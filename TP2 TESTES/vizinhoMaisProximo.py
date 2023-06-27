import time

def vizinhoMaisProximo(G):
    inicio = time.time()
    print("Processando . . .")
    u = 0       #Vertice atual
    C = []      #Caminho final
    Q = []      #Lista de vertices à serem processados
    custo = 0

    for i in range(len(G)): #Criando uma lista de 0 à len(G)
        Q.append(i)
    Q.remove(u)             #Removendo o elemento u pois não precisamos cacular ele

    while len(Q) != 0:      #Enquanto a lista de vertices à serem processados for diferente de nulo
        min = float("inf")
        pos = 0
        for i in Q:
            if min > G[u][i] and G[u][i] != 0:  #Testa vizinho mais próximo
                min = G[u][i]
                pos = i
        custo += min

        C.append((u, pos))      #Adiciona o vizinho mais próximo a lista
        Q.remove(pos)           #Remove o vertice ja calculado
        u = pos                 #Atualiza o vertice a ser calculado
        aux = time.time()

        if aux - inicio >= 600: #Retorna melhor rota em até 10 min
            custo += G[u][0]
            C.append((u, 0))  # Adiciona o ultimo vertice para fechar o ciclo
            fim = time.time()

            print("Melhor Rota em ate 10 min:")
            print("Rota: ", C)
            print("Custo: {:.2f}".format(custo))
            print("Tempo:", fim - inicio, "s")
            return fim - inicio

    custo += G[u][0]
    C.append((u, 0))            #Adiciona o ultimo vertice para fechar o ciclo
    fim = time.time()

    print("Rota: ", C)
    print("Custo: {:.2f}". format(custo))
    print("Tempo:", fim - inicio, "s")

    return fim - inicio