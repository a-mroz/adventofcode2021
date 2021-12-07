import fileinput
from collections import Counter

def parse():
    for l in fileinput.input():
       return [int(f) for f in l.split(',')]

def task1(crabs):
    minCost = float('inf')
    for i in range(max(crabs)):
        cost = sum([abs(crab - i) for crab in crabs ])
        if cost < minCost:
            minCost = cost

    return minCost

def task2(crabs):
    minCost = float('inf')
    for i in range(max(crabs)):
        cost = sum([ (abs(crab - i) * (abs(crab - i) + 1) / 2) for crab in crabs ])
        if cost < minCost:
            minCost = cost

    return int(minCost)

input = parse()

print(task1(input))
print(task2(input))
