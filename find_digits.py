# Exercise: Find digits
# URL: https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
# Description: For a given integer n, count how many of its digits (ignoring zero) evenly divide n

def findDigits(n):
    count = 0
    for d in str(n):
        if d != '0' and n % int(d) == 0:
            count += 1
    return count
