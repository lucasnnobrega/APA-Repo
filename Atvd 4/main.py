# Python program for implementation of heap Sort
# Um programa em Python para a implementação do heap sort 

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

def heapify(arr, n, i):
    '''
    Arguments:
    Para heapify arvore interior com raiz no index i
    n eh o tamanho da heap
    '''
    esquerda = 2 * i + 1    # Isso causa uma operação
    direita = 2 * i + 2     # prefixa
 
    # Ver se o filho esquerdo da raiz existe e se
    # é maior que a raiz    
    if esquerda < n and arr[i] < arr[esquerda]:
        maior = esquerda
    else:
        maior = i  # Inicializar com o maior sendo a raiz
    
    # Ver se o filho direito da raiz existe e se
    # é maior que a raiz
    if direita < n and arr[maior] < arr[direita]:
        maior = direita
     
    # Mudar a raiz, se necessario
    if maior != i:
        arr[i],arr[maior] = arr[maior],arr[i]  # troque os valores

        # Heapify a raiz.
        heapify(arr, n, maior)
 

def Build_Max_Heap(arr):
    # Construir uma maxheap, pode ser chamada de BUILD-MAX-HEAP
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
# A funcao principal para ordenar uma lista de tamanho n
def heapSort(arr):

    n = len(arr)

    Build_Max_Heap(arr)    
    # Extrair os elementos de um por um
    for i in range(n-1, 0, -1):
        # Troca o valor to topo da arvore para o valor menor
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
 
def benchmark(func, lista, *kargs):
    print("\n\n" + func.__name__)
    print("Original:", lista)
    start = time.time() # Retorna em segundos
    func(lista, *kargs)
    end = time.time()   # Retorna em segundos
    print("\nTempo gasto:", end-start, "segundos")
    print("Final:   ", lista)
    print(func.__name__ + "\n\n")

a = list(b) # Obriga a criar instancias diferentes da classe list
benchmark(heapSort, a)