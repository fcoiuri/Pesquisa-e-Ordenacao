import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit


numbers = [100000, 200000, 400000, 500000, 1000000, 2000000]

def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Bucket Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def bucketSort(vetor):
    maior = max(vetor)
    tamanho = 6
    aux = maior/tamanho
 
    sorteado = [[] for _ in range(tamanho)]


    for i in range(tamanho):
        auxiliar = int(vetor[i]/aux)

        if auxiliar != tamanho:          

            sorteado[auxiliar].append(vetor[i])
            
        else:
            
            sorteado[tamanho - 1].append(vetor[i])
        
    while i in range(tamanho):
        insertionSort(sorteado[i])
        i = i + 1
    resposta = []
    while i in range(tamanho):
        resposta = resposta + sorteado[i]
        i = i + 1
 
    return resposta

def insertionSort(vector):
    for i in range(1, len(vector)):
        valor_atual = vector[i]
        posi = i

        while(posi>0 and vector[posi-1]>valor_atual):
            vector[posi] = vector[posi-1]
            posi = posi-1

        vector[posi] = valor_atual

    return(vector)


def Imprime(nums0):
    nums = nums0
    time = []
    for r in nums:
        vector = geraLista(r)
        tempo = timeit.timeit("bucketSort({})".format(vector),setup="from __main__ import bucketSort",number=1)
        time.append(tempo)

    drawGraph(nums, time, nam="BucketSort.png")

Imprime(numbers)
