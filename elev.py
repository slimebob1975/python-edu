from turtle import *

def line(x1,y1,x2,y2):
    pu()
    goto(x1,y1)
    pd()
    goto(x2,y2)
    pu()

setworldcoordinates(-10,-10,10,10)
speed(100)
for i in range (0,11):
    line(-i,-10,-i,10)
for i in range (0,11):
    line(i,10,i,-10)
for i in range (0,11):
    line(-10,-i,10,-i)
for i in range (0,11):
    line(10,i,-10,i)

def fyll(x,y):
    if x > int(x+0.5):
        e = int(x)
        e += 1
    else:
        e = int(x)
    if y > int(y+0.5):
        f = int(y)
        f += 1
    else:
        f = int(y)
       

       
    pu()
    goto(e,f)
    pd()
    begin_fill()
    goto(e+1,f)
    goto(e+1,f+1)
    goto(e,f+1)
    goto(e,f)
    end_fill()    

onscreenclick(fyll)
