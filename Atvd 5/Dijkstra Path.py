# -*- coding: utf-8 -*-
"""
Created on "Mon Feb 26 11:29:23 2018"

@author: Lucas NN

"""



# Programa em Python para o algorítimo de Dijkstra 
# para o caminho mais curto. O programa recebe a 
# matriz de adjacência como representação do grafo
# e retorna o caminho

import open_file as op

#Class to represent a graph
class Graph:
 
    # Uma função para procurar o vértice com a minima distanca do conjunto de vertices
    # ainda na fila
    def minDistance(self,dist,fila):
        
        # Inicialize o valor minimo e o index minimo como -1
        minimum = float("Inf")
        min_index = -1
         
        # para a distancia array, escolhendo qual tem o mínimo valor ainda esta
        # na fila
        for i in range(len(dist)):
            if dist[i] < minimum and i in fila:
                minimum = dist[i]
                min_index = i
        return min_index
 
    # Função para mostrar o caminho da origem para j usando o array pai
    def printPath(self, parent, j):
         
        # Caso base, se j é a origem
        if parent[j] == -1 : 
            print (j, end = " ")
            return
        self.printPath(parent , parent[j])
        print (j, end = " ")
         
 
    # Uma função para mostrar o array de distancia construida
    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t  %d \t         " % (src, i, dist[i]), end = " ")
            self.printPath(parent,i)
 
    def dijkstra(self, graph, src):
 
        linha = len(graph)
        col = len(graph[0])
 
        # O array de saída. dist[i] irá armazenar a menor distância do começo até
        # i, inicializando tudo com INFINITO
        dist = [float("Inf")] * linha
 
        # Array pai que armazena a árvore de menor caminho
        parent = [-1] * linha
 
        # Distância do vértice fonte para ele mesmo é sempre 0
        dist[src] = 0
     
        # Adicione todos os vértices na fila
        fila = []
        for i in range(linha):
            fila.append(i)
             
        # Procure o menor caminho para todos os vértices
        while fila:
 
            # Pegue o vértice que possui a distancia mínima do conjunto de vertices
            # que ainda estão na fila
            u = self.minDistance(dist,fila) 
 
 
            # Remova o mínimo elemento     
            fila.remove(u)
 
            # Atualize o valor da distancia e o index do pai dos vértices adjacentes
            # dos vértitices escolhidos. Considere somente os vértices nos quais 
            # ainda estão na vila
            for i in range(col):
                '''Atualize dist[i] somente se estiver na fila, existe um vértice
                de u para i, e o peso total para o caminho para a origem para i 
                passando por u é menor que o valor corrente do dist[i]'''
                if graph[u][i] and i in fila:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
 
 
        # Imprima o array de distância construida
        self.printSolution(dist,parent)
 
g= Graph()
 
graph = op.grafos_matriz['dij40']
 
g.dijkstra(graph,0)
