# Smallest multiple: https://projecteuler.net/problem=5
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys
sys.path.append('./eulerhelpers')

from prime import primeFactors

dictofPrimesBelow20 = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0}

for i in xrange(2, 21):
    i_primeFactors = primeFactors(i)
    i_dict = dict()
    for j in i_primeFactors:
        i_dict[j] = i_dict.get(j, 0) + 1
    for k in sorted(i_dict):
        if i_dict[k] > dictofPrimesBelow20[k]:
            dictofPrimesBelow20[k] = i_dict[k]

# print dictofPrimesBelow20
result = 1
for i in sorted(dictofPrimesBelow20):
    result *= i ** dictofPrimesBelow20[i]

print result


def bruteforce():

    notSolved = True
    i = 1
    while notSolved:
        if i % 20 == 0:
            if i % 19 == 0:
                if i % 18 == 0:
                    if i % 17 == 0:
                        if i % 16 == 0:
                            if i % 15 == 0:
                                if i % 14 == 0:
                                    if i % 13 == 0:
                                        if i % 12 == 0:
                                            if i % 11 == 0:
                                                if i % 10 == 0:
                                                    notSolved = False 
               
        i += 1
    print i - 1

# bruteforce()

