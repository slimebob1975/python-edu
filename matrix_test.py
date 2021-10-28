#!/usr/bin/python
# Script for matrix and vector operations

# Imports
import random
import time

# Routines for initiation of vectors and matrices

# Init a zero matrix of m rows and n columns
def init_zero_matrix(m,n):

    return [[0.0 for j in range(n)] for i in range(m)]

def init_zero_row_vector(n):

    return init_zero_matrix(1,n)

def init_zero_col_vector(n):

    return init_zero_matrix(n,1)

def init_random_matrix(m,n,interval=(-1.0,1.0)):

    return [[random.uniform(interval[0],interval[1]) \
             for j in range(n)] for i in range(m)]

def init_random_row_vector(n):

    return init_random_matrix(1,n)

def init_random_col_vector(n):

    return init_random_matrix(n,1)

# Routines for matrix addition and subtraction
def matrix_addition(a,b):

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print('ERROR! Matrices are not of same dimensions')
        return [[]]
    
    c = init_zero_matrix(len(a), len(a[0]))
    for i in range(0,len(c)):
        for j in range(0,len(c[0])):
            c[i][j] += a[i][j] + b[i][j]

    return c

# Routines for matrix multiplication
# Variant stands for order in three-nested loop:
#   variant = 0 gives simple ijk algorithm (defaut)
#   variant !=0 gives simple ikj algorithm
def matrix_multiply(a,b,variant=0):

    if len(a[0]) != len(b):
        print('ERROR! Matrix dimensions are not compatible')
        return [[]]

    # Extract dimensions
    m = len(a)
    n = len(b)      # Or len(a[0])
    p = len(b[0])

    # Prepare output matrix
    c = init_zero_matrix(m,p)

    # Make multiplication and save result in c
    # Default is to use simple ijk-algorithm
    if variant == 0:
        for i in range(0,m):
            for j in range(0,p):
                for k in range(0,n):
                    c[i][j] += (a[i][k]*b[k][j])
    else:
        for i in range(0,m):
            for k in range(0,n):
                for j in range(0,p):
                    c[i][j] += (a[i][k]*b[k][j]) 

    # Return output matrix
    return c

# Routines for printing matrices
def print_matrix(a,name='matrix',outputformat='f'):
    print("\n" + str(name) + " = \n")
    for row in a:
        for col in row:
            if col >= 0:
                print((' {:<10.4'+outputformat+'}').format(col),end="")
            else:
                print(('{:<11.4'+outputformat+'}').format(col),end="")
        print("\n", end="") # Make sure to break the line after each row
    print("\n", end="") # Make sure to break the line after the last row

# Main program
def main():
    print('Give matrix dimensions: m,n,p!')
    m = int(input('m = '))
    n = int(input('n = '))
    p = int(input('p = '))

    print('Initializing test matrices...hang on!')
    t1 = time.time()
    a = init_random_matrix(m,n)
    b = init_random_matrix(n,p) 
    t2 = time.time()-t1
    print('Initialization took {:5.3f} seconds.'.format(t2))
    print('Performing matrix multiplication...just a moment!')
    t1 = time.time()
    c = matrix_multiply(a,b,1)
    t2 = time.time()-t1
    print('Multiplication took {:5.3f} seconds.'.format(t2))

# Start main program
if __name__ == "__main__":
    main()
