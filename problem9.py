"""
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time
 
def prod_triplet_w_sum(n):
    for i in range(1,n,1):
        for j in range(1,n-i,1):
            k = n-i-j
            if i**2+j**2==k**2:
                return i*j*k
    return 0
 
start = time.time()
product = prod_triplet_w_sum(1000)
elapsed = (time.time() - start)
 
print ("found %s in %s seconds" % (product,elapsed))