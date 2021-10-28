# Module for plotting functions
import myplot as mp

# Main program
def main():
    """The main test program"""
    xval = []
    yval1 = []
    x = 0
    while x <= 20:
        xval.append(x)
        y = 100 * 0.8 ** x
        yval1.append(y)
        x += 1
    mp.plotsetup(mywidth = 600, myheight = 600, xmin = 0, ymin = 0, \
              xmax = 22, ymax = 110, xgridsize = 1, ygridsize = 10,
              xlabel = 'Bounce', ylabel = 'Height', plottitle = 'Bouncing ball' )
    mp.plotcurve(xval, yval1, 'red')
    mp.plotlegend(xpos = 120, ypos = 35, \
               texts = ['y = 100 * 0.8 ** x'], \
               clrs = ['red'])
    mp.plotfinish()
   
# Start main program
if __name__ == "__main__":
    main()
