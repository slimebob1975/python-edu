from turtle import *
import colorsys
import math

HEIGHT = 600
WIDTH = 600
XMIN = -2.0
XMAX = 0.6
YMIN = -1.25
YMAX = 1.25
RES = min((XMAX-XMIN)/WIDTH,(YMAX-YMIN)/HEIGHT)
#RES = 0.01 # for faster demo
NMAX = 1024
PNSZE = 1

def mandelbrot(c):
    a,b = c
    z = (0.0,0.0)
    n = 0
    sqabs = 0    
    while n < NMAX and sqabs < 4:
        z = z[0]**2 - z[1]**2 + a, 2*z[0]*z[1] - b
        sqabs = z[0]**2 + z[1]**2
        n += 1
    if n==NMAX:
        return n
    else:
        return (n + 1 - math.log(math.sqrt(a**2+b**2),2)) 

def mandelbrotcolor(iter):
    if iter == NMAX:
        return (0,0,0)
    else:
        rgb = colorsys.hsv_to_rgb((iter)/NMAX,1.0,1.0)
        rgb = int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)
        return rgb

def putpixel(x,y,clr):
    pu()
    goto(x,y)
    pd()
    dot(clr)
    pu()

def zoomin(x,y):

    global XMAX,XMIN,YMAX,YMIN,RES
    xlen = XMAX-XMIN
    ylen = YMAX-YMIN

    XMAX = x + xlen / 4
    XMIN = x - xlen / 4
    YMAX = y + ylen / 4
    YMIN = y - ylen / 4
    RES = RES / 2
    
    draw()

def zoomout(x,y):

    global XMAX,XMIN,YMAX,YMIN,RES
    xlen = XMAX-XMIN
    ylen = YMAX-YMIN

    XMAX = x + xlen
    XMIN = x - xlen
    YMAX = y + ylen
    YMIN = y - ylen
    RES = RES * 2 

    draw()

def environment():
    setup(width=WIDTH,height=HEIGHT)

def draw():
    setworldcoordinates(XMIN, YMIN, XMAX, YMAX)
    print('World coordinates: xmin=', XMIN, ',xmax=', XMAX, 'ymin=', \
          YMIN, 'ymax=', YMAX)
    print('Resolution = ', RES)

    pensize(PNSZE)
    colormode(255)
    speed(1)
    tracer(1000)
    ht()
    clear()

    a = XMIN
    while a < XMAX:
        b = YMIN
        while b < YMAX:
            c = (a,b)
            n = mandelbrot(c)
            clr = mandelbrotcolor(n)
            putpixel(a,b,clr)
            b += RES
        a += RES
    update()

    onscreenclick(zoomin,btn=1,add=True)
    onscreenclick(zoomout,btn=3,add=False)
        
    done()      

def main():
    environment()
    draw()

if __name__ == "__main__":
    main()
    exit()

