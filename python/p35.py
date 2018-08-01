# Circular primes
# Problem 35 
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from eulerhelpers.prime import sieve


def rotateNum(num):
    yield num
    rotations_remaining = len(str(num)) - 1
    while (rotations_remaining > 0):
        rotations_remaining -= 1
        if (str(num)[1:] + str(num)[0])[0] == "0": yield "Error"
        num = int(str(num)[1:] + str(num)[0])
        yield num


limit = 1000000
primeSet = set(sieve(limit))
circularPrimeSet = set()

for prime in primeSet:
    if prime in circularPrimeSet: continue
    testPrimes = set(rotateNum(prime))
    if testPrimes.issubset(primeSet):
        for testPrime in testPrimes:
            circularPrimeSet.add(testPrime)

print len(circularPrimeSet)