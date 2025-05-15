# Exercise: Beautiful Days at the Movies
# URL: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
# Description: Count the number of beautiful days between two given days.

def beautifulDays(i, j, k):
    def reverse(n):
        return int(str(n)[::-1])
    
    count = 0
    for day in range(i, j + 1):
        if abs(day - reverse(day)) % k == 0:
            count += 1
    return count
