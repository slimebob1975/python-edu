# sorted vs mergesort
import myplot as mp
from time import time
from random import randrange

MIN = 10000
MAX = 200000
STEP = 10000

def sortOfMergesort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2 - 1
        array1 = sortOfMergesort(array[:mid+1])
        array2 = sortOfMergesort(array[mid+1:])
        array3 = []
        i,j = 0,0
        for k in range(len(array)):
            if i < len(array1) and j < len(array2):
                if array1[i] < array2[j]:
                    array3.append(array1[i])
                    i += 1
                else:
                    array3.append(array2[j])
                    j += 1
            elif i < len(array1):
                array3.append(array1[i])
                i += 1
            else:
                array3.append(array2[j])
                j += 1
        return array3

def main():

    sizes = []
    timings1 = []
    timings2 = []

    for i in range(MIN,MAX+1,STEP):
        sizes.append(i)
        lista1 = [randrange(1,MAX) for i in range(i)]
        lista2 = lista1.copy()
        t0 = time()
        lista1 = sorted(lista1)
        t = time() - t0
        timings1.append(t)
        print("Att sortera {} heltal tog sorted {:.3f} sekunder".format(i,t))
        t0 = time()
        lista2 = sortOfMergesort(lista2)
        t = time() - t0
        timings2.append(t)
        print("Att sortera {} heltal tog mergesort {:.3f} sekunder".format(i,t))
    print("Plottar resultat...")
    mp.plotsetup(mywidth = 600, myheight = 600, xmin = 0, ymin = 0, \
                 xmax = MAX, ymax = max(timings2), xgridsize = STEP, \
                 ygridsize = max(timings2) / 20, xlabel = 'n', \
                 ylabel = 'time (sec.)', \
                 plottitle = 'Sorted vs Mergesort' )
    mp.plotcurve(sizes, timings1, 'red')
    mp.plotcurve(sizes, timings2, 'blue')
    mp. plotlegend(xpos = MAX/2, ypos = max(timings2), \
                   texts = ['sorted','mergesort'], clrs = ['red','blue'])
    mp.plotfinish()
        
main()
