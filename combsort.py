# Combsort
from time import time
from random import randrange
import myplot as mp

MIN = 1000
MAX = 20000
STEP = 1000

def combsort(lista):
    gap = len(lista)
    changes = True
    while gap > 1 or changes:
        if gap > 1:
            gap = max(1,int(gap/1.3))
        changes = False
        i = 0
        #print (gap,changes,i)
        while i + gap <= len(lista)-1:
            #print("\t",i,gap,changes,lista[i],lista[i+gap])
            if lista[i] > lista[i+gap]:
                lista[i],lista[i+gap] = lista[i+gap],lista[i]
                changes = True
                #print("\t\t",changes)
            i += 1
    return lista

def main():

    sizes = []
    timings = []

    for i in range(MIN,MAX+1,STEP):
        sizes.append(i)
        lista = [randrange(1,MAX) for i in range(i)]
        t0 = time()
        lista = combsort(lista)
        t = time() - t0
        timings.append(t)
        print("Att sortera {} heltal tog {:.3f} sekunder".format(i,t))
    print("Plottar resultat...")
    mp.plotsetup(mywidth = 600, myheight = 600, xmin = 0, ymin = 0, \
                 xmax = MAX, ymax = max(timings), xgridsize = STEP, \
                 ygridsize = 2*min(timings), xlabel = 'n',
                 ylabel = 'time (sec.)', plottitle = 'Combsort' )
    mp.plotcurve(sizes, timings, 'red')
    mp.plotfinish()
        
main()
