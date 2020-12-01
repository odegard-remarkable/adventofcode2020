from itertools import combinations
from math import prod

with open ("input.txt", "r") as f:
    entries = [int(i) for i in f.read().strip().splitlines()]

def findCombinations(numberOfEntries):
    for combination in combinations(entries, numberOfEntries):
        if sum(combination) == 2020:
            return prod(combination)

print(findCombinations(2))
print(findCombinations(3))