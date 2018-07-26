# -*- encoding: utf-8 -*-
# Quadratic primes: https://projecteuler.net/problem=27
# Problem 27 
# Euler discovered the remarkable quadratic formula:
# 
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
# 
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
# 
# n2+an+b, where |a|<1000 and |b|≤1000
# 
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

from eulerhelpers.prime import sieve

bigPrimeSet = set(sieve(10000))
primeSet = set(sieve(1000))
unevenSet = set(num for num in xrange(-999, 1000) if num % 2 == 1)

count = 0
count_prod = 0

for a in unevenSet:
    for b in primeSet:
        for n in xrange(1000):
            test = n**2 + a*n + b
            if test in bigPrimeSet:
                if n > count:
                    count = n
                    count_prod = a*b
                    
            else: break
            
print count, count_prod