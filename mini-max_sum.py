# Exercise: Mini-Max Sum
# URL: https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
# Description: Given five positive integers, find the minimum and maximum values 
# that can be calculated by summing exactly four of the five integers

def miniMaxSum(arr):
    total = sum(arr)
    min_val = total - max(arr)
    max_val = total - min(arr)
    print(min_val, max_val)
