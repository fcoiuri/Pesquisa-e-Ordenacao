from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


numbers = [10000,20000,50000,100000]

def generateList(size):
    listt = []
    for i in range(size):
        n = randint(1,100)
        if(n in listt):
          n = randint(1,100)
        listt.append(n)
    return listt

#bubblesort
def Sort(listt):
    aux = 0
    if len(listt) <= 1:
        organizado = listt
    else:
        for j in range(0,len(listt)):
            for i in range(0,len(listt)-1):
                if listt[i]>listt[i+1]:
                    aux = listt[i+1]
                    listt[i+1] = listt[i]
                    listt[i] = aux
                    aux+=1
        organizado = listt
    return aux

mpl.use('Agg')

def drawGraph(x,y, xl = "Entradas", yl = "Tempos", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "B Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam) 

A = []
B = []
Z = []

for i in numbers:
    Z.append(generateList(i))
    
for i in range(len(numbers)):
    A.append(timeit.timeit("Sort({})".format(Z[i]),setup="from __main__ import generateList,Sort",number=1))
    
drawGraph(numbers,A, nam="TempoSort.png", yl="Tempo")

for i in range(len(numbers)):
    B.append(Sort(Z[i]))
    
drawGraph(numbers,B, nam="Quantidade.png", yl="Iterações")

    
