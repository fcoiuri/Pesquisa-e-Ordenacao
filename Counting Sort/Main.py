import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

numbers = [100000, 200000, 400000, 500000, 1000000, 2000000]

def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Counting Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def countingSort(vetor, top):
    n = len(vetor)
    m = top + 1
    aux = [0] * m               
    for a in vetor:
        aux[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(aux[a]): 
            vetor[i] = a
            i += 1
    return vetor

def Imprime(nums0):
    nums = nums0
    time = []
    for r in nums:
        vector = geraLista(r)
        tempo = timeit.timeit("countingSort({},{})".format(vector, r),setup="from __main__ import countingSort",number=1)
        time.append(tempo)
    drawGraph(nums, time, nam="CountingSort.png")

Imprime(numbers)
