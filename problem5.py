"""
https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divisible(t,n):
    if n > 0:
        if not (t%n):
            if divisible(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not divisible(i,20):
    i +=20

print(i)