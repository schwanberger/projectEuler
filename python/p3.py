# Largest prime factor: https://projecteuler.net/problem=3
# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?


def primeFactors(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n /= i
            
        else: i = nextPrime(i)
    
    return factors
            

def nextPrime(n):
    n += 1
    while not isPrime(n):
        n += 1

    return n


def isPrime(n):
    for i in xrange(2, int(0.5 * n) + 1):
        if n % i == 0:
            return False

    return True


print primeFactors(600851475143)
