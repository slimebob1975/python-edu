# Module for plotting functions
import myplot as mp

# Main program
def main():
    """The main test program"""
    xval = []
    yval1 = []
    x = 0
    while x <= 105:
        xval.append(x)
        y = -28*x*(x-105) / (105/2)**2
        yval1.append(y)
        x += 0.1
    mp.plotsetup(mywidth = 1000, myheight = 600, xmin = -1, ymin = -1, \
              xmax = 120, ymax = 35, xgridsize = 10, ygridsize = 3,
              xlabel = 'x', ylabel = 'y', plottitle = 'Bridge plot' )
    mp.plotcurve(xval, yval1, 'red')
    mp.plotlegend(xpos = 120, ypos = 35, \
               texts = ['-28*x*(x-105) / (105/2)**2'], \
               clrs = ['red'])
    mp.plotfinish()
   
# Start main program
if __name__ == "__main__":
    main()
