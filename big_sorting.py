# Exercise: Big sorting
# URL: https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true
# Description: Sorting a list of large numbers given as strins

def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))
