# Compute symmetric derivative of given order of function in point x:
#
#   f'(x) = (f(x+h) - f(x-h)) / 2h
#
# Higher order derivatives are computed by recursion using the
# same formula above. This version uses callback functions to
# compute the derivative.
#
# To small h gives large round-off-errors in calculations, so use with care.
# This implementation is more about proof of concept than mathematical
# stability.
#
from math import *

def dydx(func, order, x, h):
    """Recursive derivative where function is represented
       by a string and derivative is computed by callback function"""
    def derivative(func,x,h):
        return (func(x+h)-func(x-h)) / (2*h)

    if order < 1:
        print("Wrong input, order cannot be < 1!")
        return False
    else:
        if order == 1:
            # First order derivative, just compute it and return
            return derivative(func,x,h)
        else:
            # Higher order, use recursion to get to lower order
            # derivative of f(x+h) and f(x-h) in formula
            value1 = dydx(func, order-1, x + h, h)
            value2 = dydx(func, order-1, x - h, h)

            # Combine the results to combine the higher order
            # derivative
            return (value1 - value2) / (2*h)

# Evaluate function with eval
def func(x):
    return eval(function)

# Test
def main():
    global function # Make sure function is visible everywhere
    function = input("Give the function to compute derivate for: ")
    orders = int(input("Give the maximum order of derivative to compute: "))
    x = 1
    h = 10 ** (-5)

    for order in range(1,orders+1):
        print("y = {} has approx. value of dy/dx of order {} in x = {} as: {}". \
              format(function,order,x,dydx(func,order,x,h)))

# Start main program
if __name__ == "__main__":
    main()
