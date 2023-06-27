import vizinhoMaisProximo
import forcaBruta
import funcoes

cont_guloso = 0
cont_forca = 0

tam = 20
peso_max = 5

grafo = funcoes.grafo_aleatorio(tam, 1, peso_max)
print("\n-------------------Guloso-------------------")
cont_guloso += vizinhoMaisProximo.vizinhoMaisProximo(grafo)
print("\n-----------------Força-Bruta----------------")
cont_forca += forcaBruta.forcaBruta(grafo)

grafo = funcoes.grafo_aleatorio(tam, 1, peso_max)
print("\n-------------------Guloso-------------------")
cont_guloso += vizinhoMaisProximo.vizinhoMaisProximo(grafo)
print("\n-----------------Força-Bruta----------------")
cont_forca += forcaBruta.forcaBruta(grafo)

grafo = funcoes.grafo_aleatorio(tam, 1, peso_max)
print("\n-------------------Guloso-------------------")
cont_guloso += vizinhoMaisProximo.vizinhoMaisProximo(grafo)
print("\n-----------------Força-Bruta----------------")
cont_forca += forcaBruta.forcaBruta(grafo)

print("\n\nMedia guloso: ", cont_guloso/3)
print("Media forca: ", cont_forca/3)

# G = [[0.0, 2.7, 3.1, 8.8, 6.1, 5.5],
#      [2.7, 0.0, 7.0, 7.6, 3.4, 3.5],
#      [3.1, 7.0, 0.0, 2.8, 7.7, 3.0],
#      [8.8, 7.6, 2.8, 0.0, 2.5, 4.2],
#      [6.1, 3.4, 7.4, 2.5, 0.0, 1.7],
#      [5.5, 3.5, 3.0, 4.2, 1.7, 0.0]]