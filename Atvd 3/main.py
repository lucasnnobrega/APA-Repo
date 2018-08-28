# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:20:37 2018

@author: lucasnn
Programa em Python 3 para Counting Sort e Radix Sort
"""

import time
import math

with open("couting.txt","r") as f:
    """
    Com o arquivo aberto, todas as linhas estarão em f.read() como string
    depois de um separar pela quebra de linha e remover o primeiro elemento
    que indica o nº de elementos, aplicamos uma função lambda para tornar o 
    array de string em array de inteiros
    """
    # Outra implementação
    #a = [int(i) for i in f.read().split('\n')[1:]]
    b = list(map(lambda x: int(x), f.read().split('\n')[1:]))

############################### COUNTING SORT ##################################

def Counting_Sort(array, lenght_or_k):
    """
    A função que ordena uma lista em ordem crescente

    """

    # O array de saída que deve estar ordenado com os valores do array inicial
    saida = [0 for i in range(lenght_or_k)]

    # Cria um array que armazena a quantidade_de_vezes de vezes que um 
    # numero aparece
    quantidade_de_vezes = [0 for i in range(lenght_or_k)]

    # Armazena a quantidade_de_vezes de cada valor que aparece no 
    # intervalo de 0 a n ou k, perceba que esta soma é "aleatória" pois depende 
    # do valor que está dentro da célula(i).
    for i in array:
        quantidade_de_vezes[i] += 1

    # Mudar quantidade_de_vezes[i] para que quantidade_de_vezes[i] contenha a 
    # posição atual do número no array de saida
    for i in range(lenght_or_k):
        quantidade_de_vezes[i] += quantidade_de_vezes[i-1]

    # Construir o array de saida
    # Para cada índice no intervalo do comprimento do array: 
    for i in range(len(array)):
        # Pega o valor contido na posição i, procura a quantidade de vezes, decrementa
        # um devido ao index zero, retorna a posição para a saída, e armazena 
        # nesse lugar o valor contido na posição i do array inicial
        saida[quantidade_de_vezes[array[i]]-1] = array[i]
        
        #Decrementa a quantidade de vezes que um numero aparece
        quantidade_de_vezes[array[i]] -= 1

    # Copia o array de saida para o array de entrada
    for i in range(len(array)):
        array[i] = saida[i]
    return array 


# Modificação do Counting_Sort para ser utilizado no algorítimo do Radix Sort
def Counting_Sort_For_Radix(arr, ordem_numerica):
    """
    Tem particularidades devido a limitação dos valores em cada index.
    """
 
    n = len(arr)
 
    # O array de saída que deve estar ordenado com os valores do array inicial
    saida = [0] * (n)
 
    # Cria um array que armazena a quantidade_de_vezesidade de vezes que um 
    # numero aparece
    quantidade_de_vezes = [0] * (10)
 
    # Armazena a quantidade_de_vezesidade de cada valor que aparece no 
    # intervalo de 0 a n ou k
    for i in range(0, n):
        # Divide pelo numero da dezena, centena ou milhar
        index = (arr[i]/ordem_numerica) 
        quantidade_de_vezes[int( (index)%10 )] += 1
 
    # Mudar quantidade_de_vezes[i] para que quantidade_de_vezes[i] contenha a 
    # posição atual do número no array de saida
    for i in range(1,10):
        quantidade_de_vezes[i] += quantidade_de_vezes[i-1]
 
    # Construir o array de saida
    # Para cada índice no intervalo do comprimento do array: 
    #i = n-1
    #while i>=0:
    for i in range(n-1, -1, -1):
        # Alteração para a ordem da centena dezena unidade...
        index = (arr[i]/ordem_numerica)

        # Pega o valor contido na posição i, procura a quantidade de vezes, decrementa
        # um devido ao index zero, retorna a posição para a saída, e armazena 
        # nesse lugar o valor contido na posição i do array inicial
        saida[quantidade_de_vezes[int((index)%10)]-1] = arr[i]

        #Decrementa a quantidade de vezes que um numero aparece
        quantidade_de_vezes[(int(index)%10)] -= 1
        #i -= 1
    #i = 0
    # Copia o array de saida para o array de entrada
    for i in range(0,len(arr)):
        arr[i] = saida[i]
 
# Radix Sort
def radixSort(arr):
 
    # Procura o numero máximo para que seja dimensionado as ordens numericas
    max1 = max(arr)
 
    # Fazer o Counting_Sort para cada ordem dos numeros
    # em vez de passar os numeros dos digitos, a ordem numerica é passada
    ordem_numerica = 1
    while max1/ordem_numerica > 0:
        Counting_Sort_For_Radix(arr,ordem_numerica)
        ordem_numerica *= 10

'''
arr = [3, 1, 3, 5, 1, 2, 3, 4, 5, 1, 2, 3]
asd = [12, 3, 12, 32, 4, 52, 6, 12, 4, 12, 4, 12, 24, 23, 231, 123,1, 321]
if len(arr) > arr.sort.pop():
    ans = Counting_Sort(arr, len(arr))
else:
ans = Counting_Sort(arr, len(arr))
print ("Sorted character array is",ans)
radixSort(asd)
print ("Sorted character array is",asd)
'''
def benchmark(func, lista, *kargs):
    print("\n\n" + func.__name__)
    print("Original:", lista)
    start = time.time() # Retorna em segundos
    func(lista, *kargs)
    end = time.time()   # Retorna em segundos
    print("\nTempo gasto:", end-start, "segundos")
    print("Final:", lista)
    print(func.__name__ + "\n\n")

a = list(b) # Obriga a criar instancias diferentes da classe list

benchmark(Counting_Sort, a, 10000)
benchmark(radixSort, b)
