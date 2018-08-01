# Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(limit):
    
    multiples = set()
    for i in xrange(2, limit + 1):
        if i not in multiples:
            yield i  
            
            multiples.update(range(i * i, limit + 1, i))

      
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
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def genPrime():
    yield 2
    yield 3
    n = 3
    while 1:
        n += 2
        while not isPrime(n):
            n += 2
        yield n
    
