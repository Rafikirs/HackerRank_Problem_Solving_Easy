# Exercise: Repeated String
# URL: https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true
# Description: Count how many times the letter 'a' appears in the first n characters of an infinitely repeated string s

def repeatedString(s, n):
    count_a = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    return full_repeats * count_a + s[:remainder].count('a')









