# -*- coding: utf-8 -*-
"""
Created on "Mon Feb 26 11:29:23 2018"
@author: Lucas NN
"""
# Programação Dinâmica para o problema da Mochila 0-1
# Retorna o valor máximo que pode ser colocado em uma mochila de capacidade_total

"""
O problema da mochila consiste em otimizar uma função que possui as seguintes 
condições:

capacitade_total = peso máximo que a mochila consegue carregar
n = número de ítens distintos (x1, x2, ... , xn)
cada um com um respectivo peso (p1, p2, ... , pn)
e valor (v1, v2, ..., vn).

temos que maximizar a função:
valor(vetor) * numero_de_itens(vetor),  

sabendo que:
* é produto interno e 
 peso(vetor) * numero_de_itens(vetor) <= peso


Para o da mochila binária, temos a segunte condição:
xi E {0, 1}

"""

import numpy as np
import open_file as op

debug = { "K": None}

def Mochila(capacidade_total, peso_produto, valores, n_de_produtos_diferentes): 

    K = [[0 for x in range(capacidade_total+1)] \
    for x in range(n_de_produtos_diferentes+1)] 
    
    debug["K_ini"] = np.array(K)
    
    # Construir a Tabela do final para o início (técnica bottom-up)
    # para evitar chamadas recursivas
    for i in range(n_de_produtos_diferentes + 1): 
        for peso in range(capacidade_total+1): 
            if i==0 or peso==0: 
                K[i][peso] = 0
            elif peso_produto[i-1] <= peso: 
                K[i][peso] = max(valores[i-1] + K[i-1][peso-peso_produto[i-1]],  K[i-1][peso]) 
            else: 
                K[i][peso] = K[i-1][peso] 
  
    debug["K_fin"] = np.array(K)
    
    resultado = list()
    
    i = n_de_produtos_diferentes
    k = capacidade_total
    while i > 0 and k > 0:
        if K[i][k] != K[i-1][k]:
            resultado.append(i)
            i = i - 1
            k = k - peso_produto[i]
        else:
            i = i - 1
    
    debug["res"] = resultado
    
    return resultado, K[n_de_produtos_diferentes][capacidade_total] 
'''
# Programa padrão para testar a função abaixo
valores = [80, 90, 10, 120] 
peso_produto = [1, 2, 3, 4] 
capacidade_total = 5
n_de_produtos_diferentes = len(valores) 
print(Mochila(capacidade_total, peso_produto, valores, n_de_produtos_diferentes)) 
'''
for i in range(5):
    print("CUIDADO POSSIVEL ESTOURO DE MEMORIA")
    valores = op.mochilas[i][1] 
    peso_produto = op.mochilas[i][0] 
    capacidade_total = 10**(1+i)
    n_de_produtos_diferentes = len(valores) 
    print(Mochila(capacidade_total, peso_produto, valores, n_de_produtos_diferentes))


