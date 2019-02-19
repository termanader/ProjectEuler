"""
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
"""
import time

# function to factor a given positive integer n
def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
 
def sum_prime_below(n):
    prime = 2
    p = [2]
    count = 1
    iter = 2
    while iter < n:
        if is_prime(iter):
            prime = iter
            p.append(prime)
            count += 1
        iter += 1
    return sum(p)


start = time.time()
prime = sum_prime_below(2000000)
elapsed = (time.time() - start)
 
print ("found %s in %s seconds" % (prime,elapsed))
"""

import time
 
def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum
 
start = time.time()
sum = prime_sum(2000000)
elapsed = (time.time() - start)
 
print ("found %s in %s seconds" % (sum,elapsed))