# Urvalsssortering
import myplot as mp
from time import time
from random import randrange

MIN = 1000
MAX = 20000
STEP = 1000

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
    timings = []

    for i in range(MIN,MAX+1,STEP):
        sizes.append(i)
        lista = [randrange(1,MAX) for i in range(i)]
        t0 = time()
        lista = sortOfMergesort(lista)
        t = time() - t0
        timings.append(t)
        print("Att sortera {} heltal tog {:.3f} sekunder".format(i,t))
    print("Plottar resultat...")
    mp.plotsetup(mywidth = 600, myheight = 600, xmin = 0, ymin = 0, \
                 xmax = MAX, ymax = max(timings), xgridsize = STEP, \
                 ygridsize = 2*min(timings), xlabel = 'n',
                 ylabel = 'time (sec.)', plottitle = 'Mergesort' )
    mp.plotcurve(sizes, timings, 'red')
    mp.plotfinish()
        
main()
