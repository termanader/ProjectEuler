"""
https://projecteuler.net/problem=6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""
import math
import time
n = 100

def square_of_sum(num):
    sumList = []
    for i in range(1, num+1):
        sumList.append(i**2)
    return sum(sumList)
        


def sum_of_square(num):
    listSum = []
    for i in range(1, num+1):
        listSum.append(i)
    return (sum(listSum)**2)



start = time.time()
L = sum_of_square(n) - square_of_sum(n)
elapsed = (time.time() - start)
 
print ("%s found in %s seconds" % (L,elapsed))
