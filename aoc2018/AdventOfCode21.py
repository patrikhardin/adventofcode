# count amount of boxes that have the same letter appearing twice
# count amount of boxes that have the same letter appearing thrice
# multiply these two counted numbers

from collections import Counter

nBoxDouble = 0
nBoxTriple = 0

with open('input2.txt', 'r') as file:
    for line in file:
        counter = Counter(line)
        if 2 in counter.values():
            nBoxDouble += 1
        if 3 in counter.values():
            nBoxTriple += 1

print(nBoxDouble * nBoxTriple)
