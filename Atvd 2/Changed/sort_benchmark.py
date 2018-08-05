#!/usr/bin/python
#
#CAUTION THIS USE TAB AS INTENTION
#

from bench import tic, toc
from random import sample

from sorting import insertion_sort, merge_sort, quick_sort, selection_sort, python_sort
import matplotlib.pyplot as plt

name = []

plt.style.use('ggplot')

def benchmark(func):
    
    # More than 10000 become impraticable with insertion
    n = [5, 10, 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    y = []
    print(func.__name__)
    name.append(func.__name__)
    for i in n:
        unsorted = sample(range(0, i), i)
        #unsorted = [x for x in range(0,i, 1)]
        if i < 100:
            print(unsorted)
        try:                
            tic()
            func(unsorted)
            a = toc()
        except Exception as e:
            raise e
        print ("%s(%d)   \t %.4gs \t %.4gs" % (func.__name__, i,toc(), a))
        y.append(a)
        
    print(name)
    plt.plot(n,y)
    plt.scatter(n,y)
    plt.xlabel("Número de valores dos arrays")
    plt.ylabel("Tempo para ordená-los")
    plt.legend(name)
    plt.title("Algorítimos de ordenação - Lucas NN")
    #plt.xticks([i for i in range(0,10001,2000)], [0 , 10, 100, 1000, 10000])
    plt.xticks(n, rotation = 45)
    #plt.legend(func.__name__)
    #plt.show()

benchmark(insertion_sort)

benchmark(merge_sort)

benchmark(quick_sort)

benchmark(selection_sort)

benchmark(python_sort)

plt.show()

