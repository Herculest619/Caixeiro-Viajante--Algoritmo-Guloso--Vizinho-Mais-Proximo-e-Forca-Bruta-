import vizinhoMaisProximo
import forcaBruta
import funcoes

try:
    print("Nº de vertices: ", end="")
    num_vertices = int(input())
    print("Peso mínimo por padrão será: 1")
    print("Peso máximo: ", end="")
    peso_max = int(input())

    print("Algoritmo:\n\t1 Guloso\n\t2 Forca-Bruta")
    algoritmo = int(input())

    if algoritmo == 1:
        grafo = funcoes.grafo_aleatorio(num_vertices, 1, peso_max)
        print("\n-------------------Guloso-------------------")
        vizinhoMaisProximo.vizinhoMaisProximo(grafo)
    elif algoritmo == 2:
        grafo = funcoes.grafo_aleatorio(num_vertices, 1, peso_max)
        print("\n-----------------Força-Bruta----------------")
        forcaBruta.forcaBruta(grafo)
    else:
        print("Número inválido para algoritmo!")
except:
    print("Foi digitado algum caractere que não é um numero!")
