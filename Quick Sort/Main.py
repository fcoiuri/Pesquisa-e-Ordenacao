import matplotlib.pyplot as plt
from random import randint
import timeit

def drawGraph(x,y,xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Quick Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)
    
def geraLista(tam):
    lista = []
    while(len(lista) < tam):
        n = randint(1,100)
        lista.append(n)
    return lista

def listaDecrescente(tam):
    lista =[]
    while (tam > 0):
        lista.append(tam)
        tam = tam-1
    return lista

def quickSort(vetor):
    if len(vetor) <= 1: 
        return vetor
    
    pivor = vetor[len(vetor)//2]
    igual = [x for x in vetor if x == pivor]
    esquerda = [x for x in vetor if x < pivor]
    direita = [x for x in vetor if x > pivor]
 
    return quickSort(esquerda) + igual + quickSort(direita)


numbers = [100000,200000,400000,500000,1000000,2000000]


def Invertido(nums0):
    nums = nums0
    time = []
    for r in nums:
        vector = geraLista(r)
        tempo = timeit.timeit("quickSort({})".format(vector),setup="from __main__ import quickSort",number=1)
        time.append(tempo)

    drawGraph(nums, time, nam="QuickSort.png", yl="Tempo")

Invertido(numbers)

