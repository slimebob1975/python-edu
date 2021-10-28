# Compute symmetric derivative of given order of function in point x:
#
#   f'(x) = (f(x+h) - f(x-h)) / 2h
#
# Higher order derivatives are computed by recursion using the
# same formula above.
#
# To small h gives large round-off-errors in calculations, so use with care.
# This implementation is more about proof of concept than mathematical
# stability.
#
from math import sqrt, cos, sin, pi

def derivative(func, order, x, h):
    """Recursive derivative where function is represented
       by a string and derivative is computed by evaluation
       of a string"""
    if order < 1:
        print("Wrong input, order cannot be < 1!")
        return False
    else:
        if order == 1:
            # First order derivative, just use formula above
            expr = "( ( (" + func.replace('x', "(" + str(x + h) + ")") + \
                ") - (" + func.replace('x', "(" + str(x - h) + ")") + \
                ") ) / (2 * " + str(h) + " ) )"
            try:
                return eval(expr)
            except:
                print("INTERNAL error. Could not evaluate expression of order 1: ",expr)
                return False
        else:
            # Higher order, use recursion to get to lower order
            # derivative of f(x+h) and f(x-h) in formula
            expr1 = derivative(func, order-1, x + h, h)
            expr2 = derivative(func, order-1, x - h, h)

            # Combine the results to combine the higher order
            # derivative
            expr = "( ( " + str(expr1) + "-" +  str(expr2) + ")" + \
                " / (2 * " + str(h) + " ) )"
        try:
            return eval(expr)
        except:
            print("INTERNAL error. Could not evaluate expression: ",expr)
            return False

# Test
def main():
    func = "x**4 + 2*x ** 2 - 2 + sqrt(x) - sin(x)"
    x = 1
    h = 10 ** (-5)

    for order in range(1,3):
        print("y = {} has approx. value of dy/dx of order {} in x = {} as: {}". \
              format(func,order,x,derivative(func,order,x,h)))

# Start main program
if __name__ == "__main__":
    main()
