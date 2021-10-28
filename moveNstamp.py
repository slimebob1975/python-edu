from turtle import *

def moveNstamp(x,y):
    goto(x,y)
    stamp()

setup(width=500,height=550)
setworldcoordinates(-300,-300,300,300)
shape('circle')
stamp()
onscreenclick(moveNstamp)

done()
