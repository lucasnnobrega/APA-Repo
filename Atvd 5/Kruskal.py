
# Programa em python para descobrir a árvore com menor distância usando kruskal
# dado um grafo com pesos, unidirecional e multiconectado 

import open_file as op

# Classe para representar o grafo
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices # Número de vértices
        self.graph = [] # dicionario padrão para armazenar o grafo
         
  
    # function to add an aresta to graph
    # Função para adicionar uma aresta no grafo
    def adicionaAresta(self,u,v,peso):
        self.graph.append([u,v,peso])
 
    # Função que procura um conjunto do elemento i
    # (usa técnica da compreeção do caminho)
    def procura(self, pai, i):
        if pai[i] == i:
            return i
        return self.procura(pai, pai[i])

    # Uma função que faz a união de 2 conjuntos do x e do y
    def uniao(self, pai, rank, x, y):
        xraiz = self.procura(pai, x)
        yraiz = self.procura(pai, y)

        # Associe a árvore com menor rank debaixo da raiz da árvore de alto rank
        if rank[xraiz] < rank[yraiz]:
            pai[xraiz] = yraiz
        elif rank[xraiz] > rank[yraiz]:
            pai[yraiz] = xraiz
 
        # Se o rank for o mesmo, então faça um como raiz
        # e incremente seu rank para 1
        else :
            pai[yraiz] = xraiz
            rank[xraiz] += 1
 
    # Função principal que constroi a Árvore de Caminho Mínimo 
    # usando o algorítimo de Kruskal
    def KruskalMST(self):
 
        result =[] # Isso irá armazenar o valor resultante do MST
 
        i = 0 # Uma variável de indexação usada para ordenar as arestas
        e = 0 # Uma variável de indexação usada para o result[]
 
        # Passo 1: Ordene todas as arestas de forma não-decrescente em ordem
        # do seu peso. Se não conseguirmos mudar o grafo, então criamos uma
        # cópia   
        self.graph =  sorted(self.graph,key=lambda item: item[2])
 
        pai, rank = [] , [] 
        # Cria V subconjuntos com elementos únicos(floresta?) 
        for node in range(self.V):
            pai.append(node)
            rank.append(0)
     
        # Numero de arestas para ser analisadas é igual a V-1
        while e < self.V -1 :
 
            # Passo 2: Pegue a menor a aresta e incremente o index 
            # para a próxima iteração
            u,v,peso =  self.graph[i]
            i = i + 1
            x = self.procura(pai, u)
            y = self.procura(pai ,v)
 
            # Se incluir essa aresta não causa um ciclo, 
            # inclua o no próximo resultado e incremente o index
            # do resultado para a próxima aresta
            if x != y:
                e = e + 1    
                result.append([u,v,peso])
                self.uniao(pai, rank, x, y)            
            # Senão, descarte a aresta
                   
        # Imprima o conteudo do result[] para mostraar a ACM construida
        print ("As arestas seguintes estão conectadas na Árvore de Caminho Mínimo")
        for u,v,peso  in result:
            #print (str(u) + " -- " + str(v) + " == " + str(peso))
            print ("%d -- %d == %d" % (u,v,peso))
 
# Driver code
dimensao = 10

g = Graph(dimensao)
for i in range(dimensao**2):
    g.adicionaAresta(*(op.grafos_lista['dij10'][i]))
g.KruskalMST()
