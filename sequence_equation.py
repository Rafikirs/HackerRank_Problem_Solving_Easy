# Exercise: Sequence Equation
# URL: https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
# Description: Make a permutation of a list based on the positions of its elements

def permutationEquation(p):
    n = len(p)
    permuted_p = []
    
    for i in range(n):
        permuted_p.append(p.index(p.index(i+1)+1)+1)
        
    return permuted_p
