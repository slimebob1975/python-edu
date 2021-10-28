from turtle import *
import colorsys

XMIN = -2.0
XMAX = 1.0
YMIN = -1.5
YMAX = 1.5
RES = 0.01
NMAX = 360
PNSZE = 1

def mandelbrot(c):
    a,b = c
    z = (0.0,0.0)
    n = 0
    sqabs = 0    
    while n < NMAX and sqabs < 4:
        x,y = z
        z = x**2 - y**2 + a, 2*x*y - b
        sqabs = z[0]**2 + z[1]**2
        n += 1
    return n

def mandelbrotcolor(iter):
    if iter == NMAX:
        return (0,0,0)
    else:
        rgb = colorsys.hsv_to_rgb((360-iter)/360,1.0,0.5)
        rgb = int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)
        return rgb

def putpixel(x,y,clr):
    pu()
    goto(x,y)
    pd()
    dot(clr)
    pu()
          
def main():
    setup(width=600,height=600)
    setworldcoordinates(XMIN, YMIN, XMAX, YMAX)
    pensize(PNSZE)
    colormode(255)
    speed(1)
    tracer(1000)
    ht()

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
    done()

if __name__ == "__main__":
    main()
    exit()

