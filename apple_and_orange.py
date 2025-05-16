# Exercise: Apple and Orange
# URL: https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
# Description: 
# Given the locations of Sam's house, an apple tree, and an orange tree, 
# as well as the distances fruits fall from their trees, calculate how many 
# apples and oranges land on the house

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = sum(s <= a + d <= t for d in apples)
    orange_count = sum(s <= b + d <= t for d in oranges)
    print(apple_count)
    print(orange_count)
