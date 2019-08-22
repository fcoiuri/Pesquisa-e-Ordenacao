import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit


def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Shell Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def shellSort(vetor):
    meio = len(vetor) // 2
    while meio > 0:
        for i in range(meio, len(vetor)):
            val = vetor[i]
            j = i
            while j >= meio and vetor[j - meio] > val:
                vetor[j] = vetor[j - meio]
                j -= meio
            vetor[j] = val
        meio = meio // 2        
    return vetor

numbers = [100000, 200000, 400000, 500000, 1000000, 2000000]
interation =[]

def Invertido(nums0):
    nums = nums0
    time = []
    for r in nums:
        vector = geraLista(r)
        tempo = timeit.timeit("shellSort({})".format(vector),setup="from __main__ import shellSort",number=1)
        time.append(tempo)
    drawGraph(nums, time, nam = "ShellSort.png", yl="Tempo(s)")
    
Invertido(numbers)
interation = []
