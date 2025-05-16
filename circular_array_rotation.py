# Exercise: Circular Array Rotation
# URL: https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true
# Description: Rotate array a to the right k times, then return the values at the indices specified in the queries list

def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n  
    rotated = a[-k:] + a[:-k]
    return [rotated[q] for q in queries]









