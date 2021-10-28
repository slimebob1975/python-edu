from turtle import *
from time import sleep
from math import *

VOID = 0
XMIN = -1
XMAX = 1
YMIN = -1
YMAX = 1

def koch(len,dim):
    if dim == 0:
        # dim = 0 is straight line
        forward(len)
        return VOID
    else:
        # dim > 1 divide in three and make recursive call
        koch(len/3,dim-1)
        left(60)
        koch(len/3,dim-1)
        right(120)
        koch(len/3,dim-1)
        left(60)
        koch(len/3,dim-1)
        return VOID

setup(width=500,height=550)
setworldcoordinates(XMIN, YMIN, XMAX, YMAX)
pensize(1)
pencolor('blue')
speed(6)
tracer()
ht()

dims = 10
for i in range(dims+1):
    pu()
    goto(0.9*XMIN,0.9*YMAX)
    write('koch curve dim = ' + str(i), font=('Arial',10,'normal'))

    # Make a triangel of side lenght sqrt(2). Start drawing at a point
    # which is the lower left corner, and draw such that the middle point
    # of the triangle is in (0,0)
    xstart = -sqrt(2)/2
    ystart = -tan(pi/6)*sqrt(2)/2
    goto(xstart, ystart)
    pd()
    left(60)
    koch(sqrt(2),i)
    right(120)
    koch(sqrt(2),i)
    right(120)
    koch(sqrt(2),i)
    right(180)
    if i < dims:
        sleep(3)
    clear()

update()
done()
