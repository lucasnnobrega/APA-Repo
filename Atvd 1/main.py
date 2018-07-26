
#import numpy as np

import time

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
    

def insertion_sort( lista ):
  for i in range(1, len(lista)):
      # Valor a_ser_inserido
      a_ser_inserido = lista[i]
      
      # Necessario para percorrer a lista de forma reversa
      k = i
      
      # Enquanto não chegou no último valor do array e o a_ser_inserido é menor
      # que o valor da lista[k-1]
      while k > 0 and a_ser_inserido < lista[k - 1]:
          lista[k] = lista[k - 1] # mude o valor da lista
          k -= 1                  # percorrer de forma decrescente o array
          
      lista[k] = a_ser_inserido   # Coloca o valor a_ser_inserido na posição

def selection_sort(lista):
    # Percorrendo o array de forma crescente
    for i in range((len(lista) - 1)):
        # Valor do array que foi selecionado para ser verificado com os outros
        selecionado = i
        
        # Depois percorrendo com os limites i+1 até o final da lista
        for j in range(i+1, len(lista)):
            
           # Verificar se o valor do selecionado não é menor que um valor da 
           #lista, se sim o selecionado muda
           if lista[j] < lista[selecionado] :
               selecionado = j
        
        # Troca de valor usando tuplas 
        if lista[i] != lista[selecionado]:
            lista[i], lista[selecionado] = lista[selecionado], lista[i]
            
def benchmark(func, lista):
    print("\n\n" + func.__name__)
    print(lista)
    start = time.time()
    func(lista)
    end = time.time()
    print(end-start)
    print(lista)
    print(func.__name__ + "\n\n")

a = list(b) # Obriga a criar instancias diferentes da classe list

benchmark(selection_sort, a)
benchmark(insertion_sort, b)
