# Exercise: Viral Advertising
# URL: https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true
# Description: 
# Simulate a viral ad shared daily starting with 5 people. Each day, half the viewers like 
# and share it with 3 new people. Return the total number of likes after n days

def viralAdvertising(n):
    shared = 5
    cumulative_likes = 0

    for day in range(n):
        likes = shared // 2
        cumulative_likes += likes
        shared = likes * 3

    return cumulative_likes









