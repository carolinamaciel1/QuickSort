
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import itertools as it
from random import randrange
sys.setrecursionlimit(1000000)


mpl.use('Agg')

def geraLista(tam):
    lista = []
    while tam > 0:
        lista.append(tam)
        tam -= 1
    return lista


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def QuickSort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst


def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'QuickSort')
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(label)
    
x = [200000,400000,600000,800000,1000000]
x1 = [10000,20000,30000,40000,50000]

yCaso = []
yPiorCaso = []
yMedioCaso = []
yMelhorCaso = []

lista = [1, 2, 3, 4, 5, 6]
listaPermutada = list(it.permutations(lista,6))
tempos = []

for i in x:
    lista = geraLista(i)
    yCaso.append(timeit.timeit('QuickSort({})'.format(lista),setup="from __main__ import QuickSort",number=1))
    
for i in x1:    
	listaa=geraLista(i)
    listac = sorted(lista)
    listad = sorted(lista,reverse=True)
    yPiorCaso.append(timeit.timeit('QuickSort({})'.format(listad),setup="from __main__ import QuickSort",number=1))
    yMedioCaso.append(timeit.timeit('QuickSort({})'.format(listaa),setup="from __main__ import QuickSort",number=1))
    yMelhorCaso.append(timeit.timeit('QuickSort({})'.format(listac),setup="from __main__ import QuickSort",number=1))

desenhaGrafico(x,yCaso,'Quantidade','Tempo','Caso')
desenhaGrafico(x,yPiorCaso,'Quantidade','Tempo','PiorCaso')    
desenhaGrafico(x,yMedioCaso,'Quantidade','Tempo','MedioCaso')    
desenhaGrafico(x,yMelhorCaso,'Quantidade','Tempo','MelhorCaso')    

for i in listaPermutada:
    tempos.append(timeit.timeit('QuickSort({})'.format(listaPermutada),setup="from __main__ import QuickSort",number=1))
    
maxIdx = tempos.index(max(tempos))

print('Tempo mais demorado:',max(tempos))
print(listaPermutada[maxIdx])   