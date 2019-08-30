import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit


numbers = [100000, 200000, 400000, 500000, 1000000, 2000000]

def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Radix Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista


def RadixSort(lista):
    bucket = [ [],[],[],[],[],[],[],[],[],[] ]
    maximo = max(lista)
    div = 1
    
    while maximo > div:
        for numList in lista:
            bucket[int((numList/div)%10)].append(numList)

        div = div * 10
        lista = []
        for i in range(10):
            lista.extend(bucket[i])
            bucket[i] = []

def Imprime(nums0):
    nums = nums0
    time = []
    for r in nums:
        vector = geraLista(r)
        tempo = timeit.timeit("RadixSort({})".format(vector),setup="from __main__ import RadixSort",number=1)
        time.append(tempo)

    drawGraph(nums, time, nam="RadixSort.png")

Imprime(numbers)
