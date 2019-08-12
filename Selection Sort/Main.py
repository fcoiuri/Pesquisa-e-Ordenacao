import matplotlib.pyplot as plt
from random import randint, shuffle
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


#selectionsort
def Sort(vetor):
  aux=0
  for i in range(len(vetor)):
    aux22=i
    
    for j in range(i+1, len(vetor)):
        if vetor[aux22]>vetor[j]:
            aux22=j
            aux = aux+1
            
    aux11=vetor[i]
    vetor[i]=vetor[aux22]
    vetor[aux22]=aux11
    
  return aux

def drawGraph(x,y,l, xl = "Nº de Elementos", yl = "Tempo(s)", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Selection Normal")
    ax.plot(x,l, label = "Selection Invertido")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)


A1 = []
B1 = []

A2 = []
B2 = []

Numeros = []
NumerosInv = []
for i in numbers:
    Numeros.append(generateList(i))
    NumerosInv.append(listDesc(i))

for i in range(4):
  A1.append(timeit.timeit("Sort({})".format(Numeros[i]),setup="from __main__ import generateList,Sort",number=1))
  B1.append(timeit.timeit("Sort({})".format(NumerosInv[i]),setup="from __main__ import listDesc,Sort",number=1))
  
for i in range(4):
  A2.append(Sort(Numeros[i]))
  B2.append(Sort(NumerosInv[i]))
  
drawGraph(numbers,A1,B1,nam="S Sort",yl="Período")
drawGraph(numbers,A2,B2,nam="Comparações",yl="Iterações")

