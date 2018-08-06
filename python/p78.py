# Coin partitions: https://projecteuler.net/problem=78
# Problem 78 
# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
# 
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.


#         p1=1    p2=2    p3=3    p4=5    p5=7    p6=11   p7=15   p8=22
# 0.      1       1       2       3       5       7       11      15
# 00.     0       1       0       1       1       2       2       4
# 000.            0       1       0       0       1       1       1
# 0000.                   0       1       0       0       0       1
# 00000.                          0       1       0       0       0
# 000000.                                 0       0       0       0
# 0000000.                                        1       0       0
# 00000000.                                               1       0
# 000000000.                                                      1

