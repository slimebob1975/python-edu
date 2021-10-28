from turtle import *

def line(x1,y1,x2,y2):
    speed(0)
    pu()
    goto(x1,y1)
    pd()
    goto(x2,y2)
    pu()

setworldcoordinates(-30,-30,30,30)
color('blue','yellow')
pensize(2)

begin_fill()
for i in range(0,21):
    line(20-i, 0, 0, i)

for i in range(0,21):
    line(20-i, 0, 0, -i)

for i in range(0,21):
    line(-20+i, 0, 0, i)
    
for i in range(0,21):
    line(-20+i, 0, 0, -i)

end_fill()
update()
done()
