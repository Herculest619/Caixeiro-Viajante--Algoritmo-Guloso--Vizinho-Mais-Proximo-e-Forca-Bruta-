from random import randint

def grafo_aleatorio(num_vertices, PesoMin, PesoMax):
    print("\nGerando grafo . . .")
    grafo = [[0 for x in range(num_vertices)] for x in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(i):
            if i != j:
                aleatorio = randint(PesoMin, PesoMax)
                grafo[i][j] = aleatorio
                grafo[j][i] = aleatorio

    # for i in range(num_vertices):
    #     for j in range(num_vertices):
    #         print(grafo[i][j], end=" ")
    #     print()

    print("Grafo gerado!")

    return grafo