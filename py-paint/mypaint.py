# Imports
import turtle as tu
import random as rnd
import math
import os
import platform
from datetime import datetime
import time
if platform.system() == 'Windows' or platform.system() == 'Darwin':
    try:
        from PIL import Image
    except:
        print('Please wait...installing missing packages...')
        os.system('python get-pip.py')
        os.system('pip install -q PIL')
        import playsound
else:
    print('This game cannot run on platform: ',platform.system())
    exit()      

# Setup variables
XMIN = -300
XMAX = 300
YMIN = -300
YMAX = 300
BORDERSIZE = 3
PAINTWINDOWTOP = 250
PAINTWINDOWBOTTOM = -250
BUTTONSIZE = 30
CLRBUTTSZE = 15
TEXTFNTSIZE = 8
INFOTEXTFNTSIZE = 10
MAXPENSIZE = 20
MINPENSIZE = 1
DEFAULTCOLOR = 'black'

# Global variables
lastx = 0
lasty = 0
added_buttons = []
xpos = []
ypos = []
clicks = 0
undocount = 0

# Global modes
NORMAL_MODE = 0
DRAW_CIRCLE_MODE = 1
DRAW_RECTANGLE_MODE = 2
DRAW_LINE_MODE = 3
mode = NORMAL_MODE
filling_on = False

# Draws a line
def line(x1,y1,x2,y2,count=True):
    global undocount
    tu.pu()
    tu.goto(x1,y1)
    tu.pd()
    tu.goto(x2,y2)
    tu.pu()
    if count:
        undocount += 4

def save():
    filename = datetime.now().strftime("%Y-%m-%d_%H%M%S") + "_mypaint.eps"
    ts = tu.getscreen()
    ts.getcanvas().postscript(file=filename)
    #im = Image.open(filename)
    #fig = im.convert('RGBA')
    #filename2 = filename.replace('eps','png')
    #fig.save(filename2, lossless = True)
    #os.remove('./'+filename)
    #print('Successfully saved drawings to file: ',filename2)

def set_mode(inmode):
    global mode
    if inmode == 'circle':
        mode = DRAW_CIRCLE_MODE
    elif inmode == 'rectangle':
        mode = DRAW_RECTANGLE_MODE
    elif inmode == 'line':
        mode = DRAW_LINE_MODE
    else:
        mode = NORMAL_MODE  
    
def clickhandler(x,y):
    global lastx, lasty, undocount, mode, xpos, ypos, clicks
    tu.onscreenclick(None)
    if mode == NORMAL_MODE:
        clicked_button = False
        for button in added_buttons:
            if x >= button[0] and x <= button[0]+button[2] and \
               y >= button[1] and y <= button[1]+button[2]:
                clicked_button = True
                eval(button[3])
                break
        if not clicked_button:
            if y < PAINTWINDOWTOP and y > PAINTWINDOWBOTTOM:
                tu.pu()
                tu.hideturtle()
                tu.goto(x,y)
                lastx = x
                lasty = y
                tu.showturtle()
                undocount += 2
            else:
                pass
    elif mode == DRAW_CIRCLE_MODE:
        if y < PAINTWINDOWTOP and y > PAINTWINDOWBOTTOM:
            xpos.append(x)
            ypos.append(y)
            clicks += 1
            if clicks == 1:
                tu.hideturtle()
                tu.goto(x,y)
                lastx = x
                lasty = y
                tu.showturtle()
                undocount += 2
            elif clicks == 2:
                radius = distance_formula(xpos[0],ypos[0],xpos[1],ypos[1])
                if ypos[0]+radius < PAINTWINDOWTOP and \
                    ypos[0]-radius > PAINTWINDOWBOTTOM and \
                    xpos[0]+radius < XMAX and xpos[0]-radius > XMIN:
                    draw_circle(xpos[0],ypos[0],radius)
                    xpos = []
                    ypos = []
                    clicks = 0
                    set_mode('normal')
                else:
                    clicks -=1
                    xpos.pop()
                    ypos.pop()
    elif mode == DRAW_LINE_MODE:
        if y < PAINTWINDOWTOP and y > PAINTWINDOWBOTTOM:
            xpos.append(x)
            ypos.append(y)
            clicks += 1
            if clicks == 1:
                tu.hideturtle()
                tu.goto(x,y)
                lastx = x
                lasty = y
                tu.showturtle()
                undocount += 2
            elif clicks == 2:
                angle = calculate_angle(xpos[0],ypos[0],xpos[1],ypos[1])
                tu.setheading(angle)
                line(xpos[0],ypos[0],xpos[1],ypos[1])
                xpos = []
                ypos = []
                clicks = 0
                set_mode('normal')
                undocount += 1
    elif mode == DRAW_RECTANGLE_MODE:
        if y < PAINTWINDOWTOP and y > PAINTWINDOWBOTTOM:
            xpos.append(x)
            ypos.append(y)
            clicks += 1
            if clicks == 1:
                tu.hideturtle()
                tu.goto(x,y)
                lastx = x
                lasty = y
                tu.showturtle()
                undocount += 2
            else:
                angle = calculate_angle(xpos[0],ypos[0],xpos[1],ypos[1])
                tu.setheading(angle)
                line(xpos[0],ypos[0],xpos[1],ypos[1])
                xpos.pop(0)
                ypos.pop(0)
                undocount += 1
                if clicks > 4:
                    xpos = []
                    ypos = []
                    clicks = 0
                    set_mode('normal')
                    undocount += 1
    tu.onscreenclick(clickhandler)

def draghandler(x,y):
    global lastx, lasty, undocount
    tu.ondrag(None)
    if y < PAINTWINDOWTOP and y > PAINTWINDOWBOTTOM:
        tu.hideturtle()
        angle = calculate_angle(lastx,lasty,x,y)
        tu.setheading(angle)
        line(lastx, lasty, x, y, count = True)
        lastx = x
        lasty = y
        tu.showturtle()
        undocount += 2
    else:
        pass
    tu.ondrag(draghandler)

def calculate_angle(x1,y1,x2,y2):
    dist = distance_formula(x1,y1,x2,y2)
    angle = math.degrees(math.asin((y2-y1)/dist))
    if x1 >= x2:
        angle = 180-angle
    return angle

def distance_formula(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def square(x,y,size,color='white',fill=True):
    tu.pu()
    tu.goto(x,y)
    tu.pd()
    tu.setheading(0)
    if fill:
        tu.fillcolor(color)
        tu.begin_fill()
    for i in range(0,4):
        tu.forward(size)
        tu.left(90)
    if fill:
        tu.end_fill()
    tu.pu()

def draw_circle(x,y,radius):
    global undocount
    tu.pu()
    tu.goto(x,y)
    tu.fd(radius)
    tu.lt(90)
    tu.pd()
    tu.circle(radius)
    tu.pu()
    tu.goto(x,y)
    undocount += 8

def set_fill(fillmode):
    global undocount
    if not filling_on:
        if fillmode == 'onoff':
            set_filling_on(True)
            tu.begin_fill()
            tu.fillcolor(tu.pencolor())
            undocount += 2
        elif fillmode == 'do':
            pass
    else:
        if fillmode == 'onoff':
            tu.end_fill()
            undocount += 1
        elif fillmode == 'do':
            tu.end_fill()
            fclr = tu.fillcolor()
            pclr = tu.pencolor()
            if fclr == pclr:
                tu.fillcolor('white')
            tu.begin_fill()
            undocount += 5

def addtextbutton(x,y,size,color,text,callback_func):
    square(x,y,size,color)
    added_buttons.append([x,y,size,callback_func])
    tu.pu()
    xtxtpos = x+size/2
    numslashns = text.count('\n')
    ytxtpos = y+size/2-(1+numslashns)*TEXTFNTSIZE
    tu.goto(xtxtpos,ytxtpos)
    tu.write(text, align='center', font=('Courier',TEXTFNTSIZE,'bold'))

def addsymbolbutton(x,y,size,color,symbol_func,callback_func):
    square(x,y,size,color)
    drawsymbol = symbol_func + "(" + str(x) + "," + str(y) + "," + \
                 str(size) + ")"
    eval(drawsymbol)
    added_buttons.append([x,y,size,callback_func])
    tu.pu()

def symbol_circle(x,y,buttonsize):
    clr = tu.pencolor()
    pnsze = tu.pensize()
    tu.pensize(2)
    tu.pencolor('black')
    tu.goto(x+buttonsize/2,y+2)
    tu.pd()
    tu.circle((buttonsize-4)/2)
    tu.pu()
    tu.pencolor(clr)
    tu.pensize(pnsze)

def symbol_square(x,y,buttonsize):
    clr = tu.pencolor()
    pnsze = tu.pensize()
    tu.pensize(2)
    tu.pencolor('black')
    tu.pd()
    square(x+5,y+5,buttonsize-2*5,None,False)
    tu.pu()
    tu.pencolor(clr)
    tu.pensize(pnsze)

def symbol_line(x,y,buttonsize):
    clr = tu.pencolor()
    pnsze = tu.pensize()
    tu.pensize(2)
    tu.pencolor('black')
    tu.pd()
    line(x+5,y+5,x+buttonsize-5,y+buttonsize-5)
    tu.pu()
    tu.pencolor(clr)
    tu.pensize(pnsze)

def addcolorbutton(x,y,size,color,callback_func):
    square(x,y,size,color)
    added_buttons.append([x,y,size,callback_func])
    tu.pu()

def painttopandbottomlines():
    psize = tu.pensize()
    tu.pensize(BORDERSIZE)
    line(XMIN,PAINTWINDOWTOP,XMAX,PAINTWINDOWTOP, count=False)
    line(XMIN,PAINTWINDOWBOTTOM,XMAX,PAINTWINDOWBOTTOM, count=False)
    tu.pensize(psize)

def putinfotext(x,y,text,alignme):
    xold,yold = tu.pos()
    tu.goto(x,y)
    clr = tu.pencolor()
    tu.pencolor('black')
    tu.write(text, align=alignme, font=('Arial',INFOTEXTFNTSIZE,'bold'))
    tu.pencolor(clr)
    tu.goto(xold,yold)

def increase_pensize():
    global undocount
    tu.pensize(min(tu.pensize()+1,MAXPENSIZE))
    undocount += 1

def decrease_pensize():
    global undocount
    tu.pensize(max(tu.pensize()-1,MINPENSIZE))
    undocount += 1


def change_pen_color(color):
    global undocount
    tu.pencolor(color)
    undocount += 1

def clear():
    tu.clearscreen()
    paintprogram()

def delete():
    global undocount
    set_mode('normal')
    for i in range(0,5):
        if undocount > 0:
            tu.undo()
            undocount -= 1
        else:
            break

def set_filling_on(inmode):
    global filling_on
    filling_on = inmode

def coordinatesystem():
    tu.setup(600,600)
    tu.setworldcoordinates(XMIN,YMIN,XMAX,YMAX)

def paintprogram():
    global undocount
    tu.speed(0)
    tu.tracer(0,0)
    tu.goto(0,0)
    tu.pd()
    tu.left(45)
    tu.showturtle()
    tu.pu()
    painttopandbottomlines()
    tu.title("My simple paint program!")

    # Pensize buttons
    addtextbutton(-XMAX,YMAX-BUTTONSIZE,BUTTONSIZE,'grey','+', \
              'increase_pensize()')
    addtextbutton(-XMAX+BUTTONSIZE,YMAX-BUTTONSIZE,BUTTONSIZE,'grey','-', \
              'decrease_pensize()')
    putinfotext(-XMAX,PAINTWINDOWTOP,'Pensize',alignme = 'left')

    # Color buttons
    # First row
    addcolorbutton(XMAX-CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'black', \
              'change_pen_color(\'black\')')
    addcolorbutton(XMAX-2*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'blue', \
              'change_pen_color(\'blue\')')
    addcolorbutton(XMAX-3*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'red', \
              'change_pen_color(\'red\')')
    addcolorbutton(XMAX-4*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'green', \
              'change_pen_color(\'green\')')
    addcolorbutton(XMAX-5*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'yellow', \
              'change_pen_color(\'yellow\')')
    addcolorbutton(XMAX-6*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'purple', \
              'change_pen_color(\'purple\')')
    addcolorbutton(XMAX-7*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'orange', \
              'change_pen_color(\'orange\')')
    addcolorbutton(XMAX-8*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'white', \
              'change_pen_color(\'white\')')
    addcolorbutton(XMAX-9*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'grey', \
              'change_pen_color(\'grey\')')
    addcolorbutton(XMAX-10*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'gold', \
              'change_pen_color(\'gold\')')
    addcolorbutton(XMAX-11*CLRBUTTSZE,YMAX-CLRBUTTSZE,CLRBUTTSZE,'cyan', \
              'change_pen_color(\'cyan\')')
    
    # Second row
    addcolorbutton(XMAX-CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'maroon', \
              'change_pen_color(\'maroon\')')
    addcolorbutton(XMAX-2*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'violet', \
              'change_pen_color(\'violet\')')
    addcolorbutton(XMAX-3*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'magenta', \
              'change_pen_color(\'magenta\')')
    addcolorbutton(XMAX-4*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'navy', \
              'change_pen_color(\'navy\')')
    addcolorbutton(XMAX-5*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'skyblue', \
              'change_pen_color(\'skyblue\')')
    addcolorbutton(XMAX-6*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'turquoise', \
              'change_pen_color(\'turquoise\')')
    addcolorbutton(XMAX-7*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'lightgreen', \
              'change_pen_color(\'lightgreen\')')
    addcolorbutton(XMAX-8*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'darkgreen', \
              'change_pen_color(\'darkgreen\')')
    addcolorbutton(XMAX-9*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'chocolate', \
              'change_pen_color(\'chocolate\')')
    addcolorbutton(XMAX-10*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'brown', \
              'change_pen_color(\'brown\')')
    addcolorbutton(XMAX-11*CLRBUTTSZE,YMAX-2*CLRBUTTSZE,CLRBUTTSZE,'silver', \
              'change_pen_color(\'silver\')')

    putinfotext(XMAX,PAINTWINDOWTOP,'Colors',alignme = 'right')

    # Erase buttons
    addtextbutton(XMAX-BUTTONSIZE,YMIN,BUTTONSIZE,'red','Clr', \
              'clear()')
    addtextbutton(XMAX-16*CLRBUTTSZE,YMAX-BUTTONSIZE,BUTTONSIZE,'grey','<-', \
              'delete()')
    putinfotext(XMAX-16*CLRBUTTSZE,PAINTWINDOWTOP,'Delete',alignme = 'left')

     # Fill on/off buttons
    addtextbutton(-XMAX+7*BUTTONSIZE,YMAX-BUTTONSIZE,BUTTONSIZE,'grey','On\nOff', \
              'set_fill(\'onoff\')')
    addtextbutton(-XMAX+8*BUTTONSIZE,YMAX-BUTTONSIZE,BUTTONSIZE,'grey','Do', \
              'set_fill(\'do\')')
    putinfotext(-XMAX+8*BUTTONSIZE,PAINTWINDOWTOP,'Fill',alignme = 'center')


    # Symbol buttons
    addsymbolbutton(-XMAX+3*BUTTONSIZE,YMAX-BUTTONSIZE,BUTTONSIZE,'grey', \
                  'symbol_circle', 'set_mode(\'circle\')')
    addsymbolbutton(-XMAX+4*BUTTONSIZE,YMAX-BUTTONSIZE,BUTTONSIZE,'grey', \
                  'symbol_square', 'set_mode(\'rectangle\')')
    addsymbolbutton(-XMAX+5*BUTTONSIZE,YMAX-BUTTONSIZE,BUTTONSIZE,'grey', \
                  'symbol_line', 'set_mode(\'line\')')
    putinfotext(-XMAX+3*BUTTONSIZE,PAINTWINDOWTOP,'Forms',alignme = 'left')

    # Exit button
    addtextbutton(XMIN,YMIN,BUTTONSIZE,'grey','Exit', 'exit()')

    # Save button
    addtextbutton(0,YMIN,BUTTONSIZE,'white','eps', 'save()')

    # Preparation, last steps
    tu.pensize(MINPENSIZE)
    tu.color(DEFAULTCOLOR,DEFAULTCOLOR)
    tu.goto(0,0)
    set_mode('normal')
    set_filling_on(False)

    # Event handlers
    tu.onscreenclick(clickhandler)
    tu.ondrag(draghandler)

    # Set variables for deletion, and deactivate tracer for more interactive
    # drawings
    undocount = 0
    tu.tracer(n=1, delay=1)
    tu.update()
    tu.mainloop()

def main():
    coordinatesystem()
    paintprogram()

main()
