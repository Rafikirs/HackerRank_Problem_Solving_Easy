# Exercise: Strange counter
# URL: https://www.hackerrank.com/challenges/strange-code/problem?isFullScreen=true
# Description: Given a strange way to count, find the new value of a given time

def strangeCounter(t):
    n = math.ceil(math.log(t/3 + 1)/math.log(2))
    base = (2**n - 1)*3
    diff = base - t
    return diff + 1
