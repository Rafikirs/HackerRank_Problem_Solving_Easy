# Exercise: Cut the sticks
# URL: https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true
# Description: 
# Repeatedly cut sticks by the length of the shortest stick, discard the shortest sticks, 
# and record the number of sticks before each cut until none remain

def cutTheSticks(arr):
    result = []
    arr.sort()
    while arr:
        result.append(len(arr))
        cut_length = arr[0]
        arr = [x - cut_length for x in arr if x - cut_length > 0]
    return result









