# Exercise: Subarray Division
# URL: https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
# Description: 
# Lily wants to give Ron a contiguous segment of a chocolate bar where the number of squares equals 
# his birth month m and the sum of values equals his birth day d. 
# The task is to count how many such segments exist

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count
