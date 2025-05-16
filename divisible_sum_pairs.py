# Exercise: Divisible Sum Pairs
# URL: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
# Description: Count the number of pairs (i, j) with i < j such that the sum of ar[i] + ar[j] is divisible by k.

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count
