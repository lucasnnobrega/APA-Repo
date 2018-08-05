
#import numpy as np

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

######################## MERGE SORT ###########################################

def merge_sort(m):
    """
    Função homônima parecida com o MatLab
    Pior Caso: O(n*Log(n))
    
    Argumentos
    ---------
    m
    
    Parametros
    ----------
    m : lista 
        Lista a ser ordenada
        
    Exemplos
    ---------
        merge_sort([4,7,8,3,2,9,1]) => [1,2,3,4,7,8,9]

    Retorno
    -------
    Retorna a lista ordenada.
    """

    comprimento = len(m)

    if comprimento == 1:
        return m

    mid = int(math.floor(comprimento / 2))

    esquerda = merge_sort(m[0:mid])
    direita = merge_sort(m[mid:comprimento])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    """
    Une duas listas ordenadas

    Parâmetros
    ----------
    esquerda  - Uma lista ordendada.
    direita - Uma lista ordenada.

    Examples

        merge([2,4],[1,6])
        # => [1,2,4,6]

    Retorna uma lista resultante da operação de união
    """

    merged = []

    # while at least one list has elements
    while esquerda or direita:

        if esquerda and direita:
            if esquerda[0] <= direita[0]:
                key = esquerda.pop(0)
            else:
                key = direita.pop(0)
        elif esquerda:
            key = esquerda.pop(0)
        else:
            key = direita.pop(0)

        merged.append(key)

    return merged

###############################################################################
            
######################## QUICK SORT ###########################################

def quick_sort(m):
    """
    Ordena uma lista utilizando o algorítimo quick sort
    Pior Caso: O(n^2) o número a ser analisado está em uma das pontas

    Parametros
    ----------
    m - Lista desordenada

    Exemplo
    --------
        quick_sort([4,7,8,3,2,9,1])
        # => [1,2,3,4,7,8,9]

    

    Returns the sorted list.
    """

    if len(m) <= 1:
        return m

    pivot = m.pop()
    menor_que = []
    maior_que = []

    for i in m:
        if i <= pivot:
            menor_que.append(i)
        else:
            maior_que.append(i)

    return quick_sort(menor_que) + [pivot] + quick_sort(maior_que)


###############################################################################
def benchmark(func, lista):
    print("\n\n" + func.__name__)
    print("Original:", lista)
    start = time.time() # Retorna em segundos
    func(lista)
    end = time.time()   # Retorna em segundos
    print("\nTempo gasto:", end-start, "segundos")
    print("Final:", lista)
    print(func.__name__ + "\n\n")

a = list(b) # Obriga a criar instancias diferentes da classe list

benchmark(merge_sort, a)
benchmark(quick_sort, b)
