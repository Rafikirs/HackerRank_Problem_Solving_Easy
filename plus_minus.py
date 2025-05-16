# Exercise: Plus Minus
# URL: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
# Description: Given an array of integers, calculate the ratios of its elements that are positive, negative, and zeros

def plusMinus(arr):
    n = len(arr)
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)
    
    print(pos / n)
    print(neg / n)
    print(zero / n)
