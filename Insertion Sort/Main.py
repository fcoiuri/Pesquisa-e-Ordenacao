import matplotlib.pyplot as plt
from random import randint
import timeit

numbers = [10000, 20000, 50000, 100000]
def generateList(size):
    listt = []
    for i in range(size):
        n = randint(1,100)
        if(n in listt):
          n = randint(1,100)
        listt.append(n)
    return listt
	
def listDesc(size):
    listt = list(range(1, size + 1))
    listt.reverse()
    return listt


def drawGraph(x,y,l, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Insertion Normal")
    ax.plot(x,l, label = "Insertion INVERTIDO")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def Sort(vector):
    aux = 0
    i = 1
    
    while(i<len(vector)):
        aux11 = vector[i]
        j = i-1

        while j >=0 and aux11 < vector[j]:
            vector[j+1] = vector [j]
            j = j-1
            aux +=1
            
        vector[j+1] = aux11
        i+=1
    return aux


A = []
B = []
Compara = []
Compara1 = []

Numeros = []
NumerosInv = []


for i in numbers:
    Numeros.append(generateList(i))
    NumerosInv.append(listDesc(i))

for i in range(4):
    A.append(timeit.timeit("Sort({})".format(Numeros[i]),setup="from __main__ import generateList,Sort", number=1))


for i in range(4):
    B.append(timeit.timeit("Sort({})".format(NumerosInv[i]),setup="from __main__ import listDesc,Sort",number=1))

for i in range(4):
    Compara.append(Sort(Numeros[i]))
    Compara1.append(Sort(NumerosInv[i]))

drawGraph(numbers, A, B, nam="Periodo.png", yl="Período")
drawGraph(numbers, Compara, Compara1, nam="Operacoes.png", yl="Comparações")

