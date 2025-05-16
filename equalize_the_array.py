# Exercise: Equalize the Array
# URL: https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true
# Description:
# Find the minimum deletions needed so all remaining elements in the array are equal 
# by removing all but the most frequent element

def equalizeArray(arr):
    from collections import Counter
    counts = Counter(arr)
    max_freq = max(counts.values())
    return len(arr) - max_freq










