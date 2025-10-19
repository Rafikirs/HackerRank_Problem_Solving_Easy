# Exercise: Manasa Stones
# URL: https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true
# Description: Find all possible arrival points based on 2 possible step lengths

from itertools import product

def stones(n, a, b):
    permutations = list(product([a, b], repeat=n-1))
    permutations = set(tuple(sorted(perm)) for perm in permutations)
    return sorted(set(sum(perm) for perm in permutations))
