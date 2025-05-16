# Exercise: Staircase
# URL: https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
# Description: Create a staircase of size of a given integer n

def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)
