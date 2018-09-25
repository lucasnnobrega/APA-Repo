# -*- coding: utf-8 -*-

import numpy as np

def ler_instancias(file_name):
    a = list()
    # Com o arquivo abrerto, percorra cada linha 
    with open(file_name, "r") as file:
        for j in range(int(file.readline())-1):
            # Adicionar os arquivos finais ao sistema
            a.append([int(i) for i in file.readline().split()])
    
    b = list()
    for j in range(len(a)):
        b.append(list([0]*(j+1)) + a[j])
    b.append([0]*(len(a)+1))
    
    matriz_original = np.array(b)
    
    matriz_real = matriz_original + matriz_original.transpose()
    
    return matriz_real
file_names = ["./instâncias/dij10.txt",
              "./instâncias/dij20.txt",
              "./instâncias/dij40.txt",
              "./instâncias/dij50.txt"]
grafos_matriz = {
            "dij10":np.array(0),
            "dij20":np.array(0),
            "dij40":np.array(0),
            "dij50":np.array(0),
        }
for names,grafo in zip(file_names,grafos_matriz):
    grafos_matriz[grafo] = ler_instancias(names)
    
grafos_lista = {
            "dij10":list(),
            "dij20":list(),
            "dij40":list(),
            "dij50":list(),        
        }

# Por causa das matrizes serem simétricas é possivel fazer isso
for grafo in grafos_matriz:
    for i in range(grafos_matriz[grafo].shape[0]):
        for j in range(grafos_matriz[grafo].shape[1]):
            #print(i,j,grafos_matriz[grafo][i][j], sep=" ---- ")
            grafos_lista[grafo].append([i, j, grafos_matriz[grafo][i][j]])