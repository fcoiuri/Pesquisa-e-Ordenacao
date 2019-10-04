import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit


def drawGraph(x,y, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "SemNome Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def SemNomeSort(vetor):
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
        quickSort(sorteado[i])
        i = i + 1
    resposta = []
    while i in range(tamanho):
        resposta = resposta + sorteado[i]
        i = i + 1
 
    return resposta

def quickSort(vetor):
    if len(vetor) <= 1: 
        return vetor
    '''
    No  Quick o vetor pode ser o primeiro elemto, o ultimo elemento, o elemento do meio ou o randomico 
    ao contrario do quick sort, o pivo sempre sera a primeira posicao 
    '''
    #pivor = vetor[len(vetor)//2]
    pivor = vetor[0] #pivo sempre a primeira posicao 
    igual = [x for x in vetor if x == pivor]
    maior = [x for x in vetor if x < pivor]
    menor = [x for x in vetor if x > pivor]
 
    return quickSort(maior) + igual + quickSort(menor)


numbers = [1000,2000,3000,4000,5000,6000,10000]


def Imprime(nums0):
    nums = nums0
    time = []
    for r in nums:
        print(r)
        vector = geraLista(r)
        tempo = timeit.timeit("SemNomeSort({})".format(vector),setup="from __main__ import SemNomeSort",number=1)
        time.append(tempo)

    drawGraph(nums, time, nam="SemNomeSort.png")

Imprime(numbers)



