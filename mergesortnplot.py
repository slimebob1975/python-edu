# Urvalsssortering
from turtle import *
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


def line(x1,y1,x2,y2):
    pu()
    goto(x1,y1)
    pd()
    goto(x2,y2)
    pu()

def plotresults(sizes, timings):

    blocks = int((MAX-MIN+STEP) / STEP)
    timeblock = max(timings) / blocks

    setup(width=600,height=600)
    setworldcoordinates(-STEP, -timeblock, MAX+STEP, max(timings)+timeblock)
    speed(0)
    ht()

    color('black')
    mark = 0
    for i in range(0,MAX+STEP,STEP):
        line(i,max(timings),i,0)
        if mark % 2 == 0:
            pu()
            goto(i,-timeblock / 2)
            write(str(mark*STEP), align='center', font=('Arial',8,'normal'))
        mark += 1
    mark = 0
    for i in range(0,blocks):
        line(0,i*timeblock,MAX+STEP,i*timeblock)
        if mark % 2 == 0:
            pu()
            goto(-STEP / 2, i*timeblock,)
            write(str(round(mark*timeblock,2)), align='center', \
                  font=('Arial',8,'normal'))
        mark += 1

    # Mark axis
    pensize(2)
    line(0,0,0,max(timings))
    left(90)
    stamp()
    line(0,0,MAX+STEP,0)
    right(90)
    stamp()

    # Plot curve
    pu()
    goto(sizes[0],timings[0])
    color('red')
    dot()
    pd()
    pensize(2)
    for i in range(1,len(sizes)):
        goto(sizes[i],timings[i])
        dot()
    pu()

    update()
    done()

def main():

    sizes = []
    timings = []

    for i in range(MIN,MAX+1,STEP):
        sizes.append(i)
        lista = [randrange(1,MAX) for i in range(i)]
        t0 = time()
        lista =  sortOfMergesort(lista)
        t = time() - t0
        timings.append(t)
        print("Att sortera {} heltal tog {:.3f} sekunder".format(i,t))
    print("Plottar resultat...")
    plotresults(sizes, timings)
    bye()
        
main()
