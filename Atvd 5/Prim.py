# Um programa em python para a árvore de caminho mínimo de Prim
# Utiliza a matriz de adjacencia como representação do grafo
 
import sys  # Biblioteca para maximo inteiro
import open_file as of 

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
 
    # Uma função utilizada para imprimir a Arvore de Caminho Mínimo armazenada 
    # no array pai
    def printMST(self, pai):
        print ("Aresta \tPeso")
        for i in range(1,self.V):
            print (pai[i],"-",i,"\t",self.graph[i][ pai[i] ])
 
    # Uma função para procurar o vértice com valor de distância mínima, de um 
    # conjunto de vertices ainda não incluidos na árvore de caminho mínimo
    def minchave(self, chave, mstSet):
 
        # Inicializar a variavel caminho_minimo com o tamanho máximo
        caminho_minimo = sys.maxsize
 
        for v in range(self.V):
            if chave[v] < caminho_minimo and mstSet[v] == False:
                caminho_minimo = chave[v]
                min_index = v
 
        return min_index
 
    # Função para construir e imprimir a árvore de caminho mínimo representada
    # usando matriz de adjacencia
    def primMST(self):
 
        # chave values used to pick minimum weight edge in cut
        # Valores chave usadas para pegar o mínimo peso da aresta cortada
        chave = [sys.maxsize] * self.V
        pai = [None] * self.V # Array para armazenar a arvore de caminho minima construida
        chave[0] = 0   # Faça a chave 0 para que esse vértice seja escolhido como primeiro vértice
        mstSet = [False] * self.V
 
        pai[0] = -1  # Primeiro nó é sempre raiz de
 
        for _ in range(self.V):
        
            # Pegue a distância mínima do vértice do conjunto de vertices ainda 
            # não processados. u é sempre igual a src na primeira iteração
            u = self.minchave(chave, mstSet)
 
 
            # Coloque a distância minima do vértice na arvore de caminho mínimo
            mstSet[u] = True


            # Atualize o valor da distância dos vértices adjacentes dos vértices
            # escolhidos somente se a distância atual é maior que a distância nova
            # e o vértice não está na arvore de caminho mínimo
            for v in range(self.V):
                
                # graph[u][v] é não nula somente para vértices adjacentes de m
                # mstSet[v] é falso se vertices ainda não forem incluidos na Aŕvore de Caminho Minimo
                # Atualize o valor da chave somente se o grafo[u][v] é menor que chave[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and \
                   chave[v] > self.graph[u][v]:
                        chave[v] = self.graph[u][v]
                        pai[v] = u
 
        self.printMST(pai)
 
print("#"*50)
g_10 = Graph(10)
g_10.graph = of.grafos_matriz["dij10"]
g_10.primMST();
print("#"*50)
g_20 = Graph(20)
g_20.graph = of.grafos_matriz["dij20"]
g_20.primMST();
print("#"*50)
g_40 = Graph(40)
g_40.graph = of.grafos_matriz["dij40"]
g_40.primMST();
print("#"*50)
g_50 = Graph(50)
g_50.graph = of.grafos_matriz["dij50"]
g_50.primMST();
