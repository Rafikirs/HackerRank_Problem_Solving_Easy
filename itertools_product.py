# Exercise: itertools.product()
# URL: http://hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Description: Using product function from itertools


from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*product(A, B))
