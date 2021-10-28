# File connected to test 1 in programming course
import random

def checkIfPowerOf2(num):

    try:
        # Now check if num if a power of 2.
        # Do this by converting it to a binary string
        # and counting the number of bits that are 1.
        # For a power of two, there should be just one
        # such bit.
        return bin(num).count('1') == 1
    except:
        print(num,' is not a number!')
        return False

def permuteNPrint2(letters, permutation = ""):
    if len(letters) == 1:
        #print(permutation + letters)
        print(permutation + letters, end="\r"),
        return 1
    else:
        count = 0
        for i in range(len(letters)):
            permutation += letters[i]
            subcount = permuteNPrint2(letters[:i]+letters[i+1:],permutation)
            count += subcount
            permutation = permutation[:-1]
        return count

def rfac(n):
    if n == 1:
        return 1
    else:
        return n * rfac(n-1)

# Iterativ fakultet
def nfac(n):
    fac = 1
    for i in range(2,n+1):
        fac *= i
    return fac


def sortofquicksort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0],array[1] = array[1],array[0]
        return array
    else:
        pivot = sum(array) / len(array)
        split = len(array)-1
        i = 0
        while i < len(array):
            if array[i] > pivot and i <= split:
                array.append(array.pop(i))
                split -= 1
            else:
                i += 1
        if split < len(array)-1:
            return sortofquicksort(array[:split+1]) + \
                   sortofquicksort(array[split+1:])
        else:
            return array

def sortOfMergesort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2 - 1
        array1 = sortOfMergesort(array[:mid+1])
        array2 = sortOfMergesort(array[mid+1:])
        array3 = []
        i,j = 0,0
        for k in range(len(array)):
            if i < len(array1) and j < len(array2):
                if array1[i] < array2[j]:
                    array3.append(array1[i])
                    i += 1
                else:
                    array3.append(array2[j])
                    j += 1
            elif i < len(array1):
                array3.append(array1[i])
                i += 1
            else:
                array3.append(array2[j])
                j += 1
        return array3              

def fibonacci(n):
    if n < 1:
        print("Wrong input to fibonacci!")
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def tribonacci(n):
    if n < 1:
        print("Wrong input to tribonacci!")
        return -1
    elif n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

def checkIfSorted(array):
    sorted = True
    for i in range(len(array)-1):
        sorted = sorted and array[i] <= array[i+1]
    return sorted

# Test
for i in range(1,100):
    if checkIfPowerOf2(i):
        print('{} is a power of two'.format(i))

# Test
for i in range(1,13):
    print('{}! = {}'.format(i,nfac(i)))

# Test
idle = "Monty"
count = permuteNPrint2(idle)
print("The number of combinations for \"{}\" is {}".format(idle,count))

# Test sort of quicksort
for j in range(1,101):
    print("Testing sort algorithm for n=",j)
    array = []
    for i in range(random.randrange(j)):
        array.append(random.randrange(j)-i)
    #print("Unsorted=",array)
    #array = sortofquicksort(array)
    array = sortOfMergesort(array)
    #print("Sorted=",array)
    if not checkIfSorted(array):
        print("Array not sorted. Breaking!")
        break
    else:
        print("Array sorted correctly!")

# Test fibonnaci and tribonacci
for i in range(1,31):
    print("Fibonacci number ",i,": ",fibonacci(i))
for i in range(1,31):
    print("Tribonacci number ",i,": ",tribonacci(i))
