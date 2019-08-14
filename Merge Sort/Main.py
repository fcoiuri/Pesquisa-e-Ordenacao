import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Merge Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def mergeSort(vetor):
    if len(vetor)>1:
        meio = len(vetor)//2
        metade_esquerda = vetor[:meio]
        metade_direita = vetor[meio:]

        mergeSort(metade_esquerda)
        mergeSort(metade_direita)

        i=0
        j=0
        k=0

        while(i<len(metade_esquerda) and j<len(metade_direita)):
            if metade_esquerda[i] < metade_direita[j]:
                vetor[k] = metade_esquerda[i]
                i=i+1
            else:
                vetor[k] = metade_direita[j]
                j=j+1
            k=k+1

        while(i< len(metade_esquerda)):
            vetor[k] = metade_esquerda[i]
            i=i+1
            k=k+1

        while(j<len(metade_direita)):
            vetor[k] = metade_direita[j]
            j=j+1
            k=k+1

        if (k == len(vetor)):
            return vetor


numbers = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]

def Invertido(nums0):
    nums = nums0
    time = []
    for r in nums:
        vector = geraLista(r)
        tempo = timeit.timeit("mergeSort({})".format(vector),setup="from __main__ import mergeSort",number=1)
        time.append(tempo)

    drawGraph(numbers, time, nam="MergeSort.png", yl= "Tempo(s)")

Invertido(numbers)

