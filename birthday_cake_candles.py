# Exercise: Birthday Cake Candles
# URL: https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
# Description: Find how many times the bigger element of a an array is repeated

def birthdayCakeCandles(candles):
    tallest = max(candles)         
    return candles.count(tallest)  
