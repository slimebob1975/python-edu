# Bubbelsortering
from time import time
from random import randrange
import myplot as mp

MIN = 1000
MAX = 10000
STEP = 1000

def bubbelsort(lista):
    while True:
        changes = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                changes = True
        if not changes:
            break
    return lista

def main():

    sizes = []
    timings = []

    for i in range(MIN,MAX+1,STEP):
        sizes.append(i)
        lista = [randrange(1,MAX) for i in range(i)]
        t0 = time()
        lista = bubbelsort(lista)
        t = time() - t0
        timings.append(t)
        print("Att sortera {} heltal tog {:.3f} sekunder".format(i,t))
    print("Plottar resultat...")
    mp.plotsetup(mywidth = 600, myheight = 600, xmin = 0, ymin = 0, \
                 xmax = MAX, ymax = max(timings), xgridsize = STEP, \
                 ygridsize = int(max(timings)/((MAX-MIN)/STEP)+1), xlabel = 'n',
                 ylabel = 'time (sec.)', plottitle = 'Bubbelsortering' )
    mp.plotcurve(sizes, timings, 'red')
    mp.plotfinish()
        
main()
