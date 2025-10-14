# Exercise: Beautiful Triplets
# URL: https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true
# Description: Counting the number of beautiful triplets in an array

def beautifulTriplets(d, arr):
    count = 0
    arr_set = set(arr)  # Pour recherche O(1)

    for num in arr:
        if (num + d in arr_set) and (num + 2 * d in arr_set):
            count += 1

    return count
