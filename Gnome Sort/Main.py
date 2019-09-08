import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

numbers = [10000, 20000, 40000, 50000, 100000, 200000]
#numbers = [100000, 200000, 400000, 500000, 1000000, 2000000]

def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Gnome Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def GnomeSort(lista):
    aux = list(lista)
    
    tamanho = len(aux)
    
    if tamanho < 2:
        return aux
    
    pivo = 0   
    aux_comprimento = len(aux)
    
    while pivo < aux_comprimento - 1:

        if aux[pivo] > aux[pivo + 1]:

            aux[pivo + 1], aux[pivo] = aux[pivo], aux[pivo + 1]

            if pivo > 0:
                pivo -= 2

        pivo += 1
        
    return aux

def Imprime(nums0):
    nums = nums0
    time = []
    for r in nums:
        print (r)
        vector = geraLista(r)
        tempo = timeit.timeit("GnomeSort({})".format(vector),setup="from __main__ import GnomeSort",number=1)
        time.append(tempo)

    drawGraph(nums, time, nam = "GnomeSort.png")

Imprime(numbers)

