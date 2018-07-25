# -*- encoding: utf-8 -*- 
# Names scores: https://projecteuler.net/problem=22
# Problem 22 Using names.txt (right click and 'Save Link/Target As...'), a 46K
# text file containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?
import string

f = open('datasets/p022_names.txt', 'r')
data = f.read()
f.close()

data = data.replace('"', '')
data = data.split(',')
data.sort()

nameScoreSum = 0
count = 1


def getNameScore(name):
    nameScore = 0
    for letter in name:
        nameScore += string.uppercase.index(letter) + 1
    return nameScore
    
        
for name in data:
    nameScoreSum += getNameScore(name) * count
    count += 1
    
print nameScoreSum