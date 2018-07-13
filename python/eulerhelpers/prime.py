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
    for i in xrange(2, int(0.5 * n) + 1):
        if n % i == 0:
            return False

    return True
