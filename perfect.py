#!/usr/bin/python
# Script for finding perfect numbers

# Imports
import math

# Subroutines below

# Routine for finding all perfect numbers up to a certain stop integer
def find_perfect_numbers_up_to(roof):
    """Find all perfect numbers up to a certain number"""

    # Prepare return list
    perfects = []
    
    # Loop from 1 to roof, including roof. If we find a number to be perfect,
    # add it to the end of the return list
    for x in range(1,roof+1):
        if is_perfect(x):
            perfects.append(x)
    return perfects

# A perfect number is defined as the sum of all its proper divisors.
def is_perfect(x):
    """Find out if a number is perfect, i.e., the sum of all its
    proper divisors"""

    # Do not consider numbers below 2
    if x < 2:
        return False

    # Find all divisors of x
    factors = find_divisors(x)

    # Sum factors
    the_sum = sum(factors)

    # Return result
    return the_sum == x

# A more perfect version of the same function as above
# A perfect number is defined as the sum of all its proper divisors.
def perfect_is_perfect(x):
    """Find out if a number is perfect, i.e., the sum of all its
    proper divisors (more perfect version)"""

    # Do not consider numbers below 2
    if x < 2:
        return False
    # Find all divisors of x, sum factors and return result
    else:
        return x == sum(find_divisors(x))

# Routine for factorizing a number in divisors
def find_divisors(x):
    """Factorizing a natural number in its divisors"""

    # Prepare output list, including trivial case
    divisors = [1]

    # Loop from 2 to half of the input number x and check
    # in each iteration for a divisor for x
    for div in range(2,math.ceil(x/2)+1):
        if x % div == 0:            # divisor found
            divisors.append(div)    # Save divisor

    # When here, all factors are found. They should also be in order
    # from the lowest to the highest by construction
    return divisors

# Main program
def main():
    """Main program for finding perfect numbers"""
    stop = int(input('Find all perfect numbers from 1 to...: '))
    perfect = find_perfect_numbers_up_to(stop)
    print('Result =',perfect)

# Starta main program
if __main__ == "__main()__":
    main()
