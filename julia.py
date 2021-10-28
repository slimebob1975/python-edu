from turtle import *
import colorsys
import math

HEIGHT = 600
WIDTH = 900
XMIN = -1.5
XMAX = 1.5
YMIN = -1.0
YMAX = 1.0
RES = min((XMAX-XMIN)/WIDTH,(YMAX-YMIN)/HEIGHT)
#RES = 0.01 # for faster demo
NMAX = 1024
PNSZE = 1
CJULIA = (-0.668683, -0.350684)

def julia(z):
    a,b = CJULIA
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

def juliacolor(iter):
    if iter == NMAX:
        return (0,0,0)
    else:
        h = (360 * math.log(iter,2)/math.log(NMAX,2) ) / 360 
        s = (100 - 100*iter / NMAX) / 100
        v = 1.0
        rgb = colorsys.hsv_to_rgb(h, s, v)
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
            z = (a,b)
            n = julia(z)
            clr = juliacolor(n)
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

