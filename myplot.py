# Module for plotting functions
import turtle as tu
from math import sqrt, sin, cos, tan

TRCER = 100
NUMDOTS = 8
FNTSIZE = 8
XMIN = 0
XMAX = 0
YMIN = 0
YMAX = 0
YTXTDISPLCMNT = FNTSIZE
MRKFNTSIZE = FNTSIZE
XTXTDISPLCMNT = 0.95
CLRDISPLCMNT = 0.75
MARKXDISPLCMNT = 0.90
MARKYDISPLCMNT = 0.30
GRIDMARKDISPLCMNT = 0.20
ONE = 1.0
HALF = 0.5
TWO = 2.0
ONEEIGHT = 1 / 8
UNDOCOUNT = 0
LEGENDTEXTS = []
LEGENDCOLORS = []

# Draw a line
def plotline(x1, y1, x2, y2, pnsize = 1):
    """Draws a straight line between two points"""
    tu.pensize(pnsize)
    tu.pu()
    tu.goto(x1,y1)
    tu.pd()
    tu.goto(x2,y2)
    tu.pu()

# Draw a dotted line
def plotdottedline(x1, y1, x2, y2, dotsize, pnsize = 1):
    """Draws a dotted line between to points"""
    tu.pensize(pnsize)
    tu.pu()
    tu.goto(x1,y1)

    dist = sqrt((x2-x1)**2 + (y2-y1)**2)
    numsteps = int(dist/dotsize)
    xdotsize = (x2-x1) / numsteps
    ydotsize = (y2-y1) / numsteps
    tu.pd()
    draw = True
    for i in range(numsteps+1):
        tu.goto(x1+i*xdotsize,y1+i*ydotsize)
        if draw:
            tu.pu()
            draw = False
        else:
            tu.pd()
            draw = True
    tu.pu()

# Set up the plot coordinate system
def plotsetup(mywidth, myheight, xmin, ymin, xmax, ymax, \
              xgridsize, ygridsize, xlabel, ylabel, plottitle):
    """Sets up coordinate system"""
    global XMIN, XMAX, YMIN, YMAX, MRKFNTSIZE

    # Basic setup
    tu.setup(width=mywidth,height=myheight)
    XMIN = xmin-xgridsize
    XMAX = xmax+xgridsize
    YMIN = ymin-ygridsize
    YMAX = ymax+ygridsize
    tu.setworldcoordinates(XMIN, YMIN, XMAX, YMAX)
    
    tu.speed(0)
    tu.ht()
    tu.tracer(0,0)

    # Adjust fontsize if gridsizes are very small
    xpixels,ypixels = tu.screensize()
    pixelsperxcoordinates = xpixels / (XMAX-XMIN)
    pixelsperycoordinates = ypixels / (YMAX-YMIN)
    xgridpixels = pixelsperxcoordinates * xgridsize
    ygridpixels = pixelsperycoordinates * ygridsize
    MRKFNTSIZE = int(min(FNTSIZE, min(xgridpixels / TWO, ygridpixels / TWO)))

    # Mark x- and y-axis
    plotline(0, ymin, 0, ymax, 2)
    tu.left(90)
    tu.stamp()
    plotline(xmin, 0, xmax, 0, 2)
    tu.right(90)
    tu.stamp()

    # Draw grid in coordinate system
    tu.pensize(1)
    tu.color('black')

    # Do x-axis in two step. First from 0 to xmax, and then from 0 to xmin
    mark = True
    xpos = 0 + xgridsize
    while xpos < xmax:
        plotdottedline(xpos, ymin, xpos, ymax, ygridsize/NUMDOTS, 1)
        if mark:
            tu.pu()
            tu.goto(xpos, -ygridsize * MARKXDISPLCMNT)
            tu.write(str(round(xpos,2)), align='center', \
                     font=('Arial',MRKFNTSIZE,'bold'))
            mark = False
        else:
            mark = True
        plotline(xpos, -ygridsize*GRIDMARKDISPLCMNT, xpos, \
                 ygridsize*GRIDMARKDISPLCMNT, 2)
        xpos += xgridsize

    mark = True
    xpos = 0 - xgridsize
    while xpos > xmin:
        plotdottedline(xpos, ymin, xpos, ymax, ygridsize/NUMDOTS, 1)
        if mark:
            tu.pu()
            tu.goto(xpos, -ygridsize * MARKXDISPLCMNT)
            tu.write(str(round(xpos,2)), align='center', \
                     font=('Arial',MRKFNTSIZE,'bold'))
            mark = False
        else:
            mark = True
        plotline(xpos, -ygridsize*GRIDMARKDISPLCMNT, xpos, \
                 ygridsize*GRIDMARKDISPLCMNT, 2)
        xpos -= xgridsize

    # Now do y-axis in the same fashion
    mark = True
    ypos = 0 + ygridsize
    while ypos < ymax:
        plotdottedline(xmin, ypos, xmax, ypos, xgridsize/NUMDOTS, 1)
        if mark:
            tu.pu()
            tu.goto(-xgridsize*MARKYDISPLCMNT, ypos - ygridsize * MARKYDISPLCMNT)
            tu.write(str(round(ypos,2)), align='right', \
                     font=('Arial',MRKFNTSIZE,'bold'))
            mark = False
        else:
            mark = True
        plotline(-xgridsize*GRIDMARKDISPLCMNT, ypos, \
                 ygridsize*GRIDMARKDISPLCMNT, ypos, 2)
        ypos += ygridsize

    mark = True
    ypos = 0 - ygridsize
    while ypos > ymin:
        plotdottedline(xmin, ypos, xmax, ypos, xgridsize/NUMDOTS, 1)
        if mark:
            tu.pu()
            tu.goto(-xgridsize*MARKYDISPLCMNT, ypos - ygridsize * MARKYDISPLCMNT)
            tu.write(str(round(ypos,2)), align='right', \
                     font=('Arial',MRKFNTSIZE,'bold'))
            mark = False
        else:
            mark = True
        plotline(-xgridsize*GRIDMARKDISPLCMNT, ypos, \
                 ygridsize*GRIDMARKDISPLCMNT, ypos, 2)
        ypos -= ygridsize

    # Set labels
    tu.title(plottitle)
    tu.goto(xmax, ygridsize / 2)
    tu.write(xlabel, align='right', font=('Arial',FNTSIZE,'bold'))
    tu.goto(xgridsize / 2, ymax-ygridsize / 2)
    tu.write(ylabel, align='left', font=('Arial',FNTSIZE,'bold'))

# Plot curve defined by list x and y and color string clr
def plotcurve(xvals, yvals, clr, pnsize = 2, stamp = True):
    """Plots a curve in the coordinate system"""

    tu.pensize(pnsize)
    tu.color(clr)
    tu.pu()
    for i in range(0,len(xvals)-1):
        tu.goto(xvals[i],yvals[i])
        if XMIN <= xvals[i] and xvals[i] <= XMAX and YMIN <= yvals[i] and \
           yvals[i] <= YMAX and XMIN <= xvals[i+1] and xvals[i+1] <= XMAX and \
           YMIN <= yvals[i+1] and yvals[i+1] <= YMAX:
            if not tu.isdown():
                tu.pd()
            if stamp:
                tu.dot()
            tu.goto(xvals[i+1], yvals[i+1])
            if stamp:
                tu.dot()
        else:
            if tu.isdown():
                tu.pu()
            tu.goto(xvals[i+1],yvals[i+1])
    tu.pu()

# Put a simple legend for the curve on the plot with upper right corner
# in (xpos, ypos), using the strings in the lists text and color
def plotlegend(xpos, ypos, texts, clrs, stamps = [False,False,False]):
    """Puts a legend in the coordinate system"""

    global UNDOCOUNT, LEGENDTEXTS, LEGENDCOLORS
    UNDOCOUNT = 0
    LEGENDTEXTS = texts.copy()
    LEGENDCOLORS = clrs.copy()

    numnewlines = 0
    for i in range(len(texts)):
        numnewlines += texts[i].count('\n') 
    xpixels,ypixels = tu.screensize()
    xcoordinatesperpixel = (XMAX-XMIN) / xpixels
    ycoordinatesperpixel = (YMAX-YMIN) / ypixels
    textrows = []
    for i in range(len(texts)):
        textrows += texts[i].split('\n')
    legendwidth = (ONE+HALF)*len(max(textrows, key=len)) * FNTSIZE*xcoordinatesperpixel
    legendheight = (TWO)*(TWO*len(textrows)-len(texts))*FNTSIZE*ycoordinatesperpixel
    
    tu.pu()
    tu.goto(xpos, ypos)
    tu.ht()
    tu.pd()
    tu.right(180)
    tu.pensize(1)
    tu.color('black','white')
    tu.begin_fill()
    tu.forward(legendwidth)
    tu.left(90)
    tu.forward(legendheight)
    tu.left(90)
    tu.forward(legendwidth)
    tu.left(90)
    tu.forward(legendheight)
    tu.end_fill()
    tu.pu()
    tu.setheading(180)

    UNDOCOUNT += 17
        
    for i in range(len(texts)):
        tu.color('black')
        numnewlines = texts[i].count('\n')
        tu.goto(xpos - legendwidth * XTXTDISPLCMNT, \
                ypos - (i+1) * legendheight / (len(texts)+1) - \
                ycoordinatesperpixel*YTXTDISPLCMNT*(1+numnewlines) )
        tu.write(texts[i], align='left', font=('Courier',FNTSIZE,'bold'))
        tu.goto(xpos - legendwidth * (ONE-XTXTDISPLCMNT),
                ypos - (i+1) * legendheight / (len(texts)+1))
        tu.color(clrs[i])
        tu.pensize(2)
        tu.pd()
        tu.forward(ONEEIGHT*legendwidth)
        if stamps[i]:
            tu.dot()
            UNDOCOUNT += 1
        tu.forward(ONEEIGHT*legendwidth)
        tu.pu()
        UNDOCOUNT += 10

    tu.onscreenclick(fun = plotmovelegend, add = False)

def plotmovelegend(x,y):
    """Moves the legend in the coordinate system"""
    print("Moving legend to coordinates: ({0:.2f},{1:.2f}) (upper right corner)". \
          format(x,y))
    #tu.speed(0)
    #tu.tracer(False)
    for i in range(UNDOCOUNT):
        tu.undo()
    plotlegend(xpos = x, ypos = y, texts = LEGENDTEXTS, clrs = LEGENDCOLORS)
    tu.update()

# Finish turtle stuffs
def plotfinish():
    """Finalizes the plot and enters standby mode"""
    tu.update()
    tu.mainloop()
    #tu.bye()
    #tu.done()

# Main program
def main():
    """The main test program"""
    xval = []
    yval1 = []
    yval2 = []
    yval3 = []
    x = -2
    while x <= 2:
        xval.append(x)
        y = sin(x**2) / x**2
        yval1.append(y)
        y = cos(x**2) / x**2
        yval2.append(y)
        y = tan(x**2) / x**2
        yval3.append(y)
        x += 0.01
    plotsetup(mywidth = 600, myheight = 600, xmin = -2, ymin = -2, \
              xmax = 2, ymax = 2, xgridsize = 0.25, ygridsize = 0.25,
              xlabel = 'x', ylabel = 'y', plottitle = 'Polynomial plot' )
    plotcurve(xval, yval1, 'red', 2, True)
    plotcurve(xval, yval2, 'blue', 2, True)
    plotcurve(xval, yval3, 'green', 2, True)
    plotlegend(xpos = 1, ypos = -1, \
               texts = ['y = sin(x**2) / x**2', \
                        'y = cos(x**2) / x**2', \
                        'y = tan(x**2) / x**2'], \
               clrs = ['red','blue','green'],
               stamps = [True, True, True])
    plotfinish()
   
# Start main program
if __name__ == "__main__":
    main()
