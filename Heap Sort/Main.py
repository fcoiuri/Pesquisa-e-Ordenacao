import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

numbers = [100000, 200000, 400000, 500000, 1000000, 2000000]

def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Heap Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista


def HeapSort(lista):
    n = len(lista)
    i = len(lista) // 2
    while (True):
        if (i > 0):
            i -= 1
            t = lista[i]
        else:
            n -= 1
            if (n == 0):
                return
            t = lista[n]
            lista[n] = lista[0]
        pai = i
        filho = (i * 2) + 1
        while (filho < n):
            if ((filho + 1 < n) and (lista[filho + 1] > lista[filho])):
                filho += 1
            if (lista[filho] > t):
                lista[pai] = lista[filho]
                pai = filho
                filho = (pai * 2) + 1
            else:
                break
        lista[pai] = t


def Imprime(nums0):
    nums = nums0
    time = []
    for r in nums:
        vector = geraLista(r)
        tempo = timeit.timeit("HeapSort({})".format(vector),setup="from __main__ import HeapSort",number=1)
        time.append(tempo)

    drawGraph(nums, time, nam="HeapSort.png")

Imprime(numbers)
