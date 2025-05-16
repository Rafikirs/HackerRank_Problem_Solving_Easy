# Exercise: Save the Prisoner!
# URL: https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true
# Description:
# Distribute m candies to n prisoners sitting in a circle starting at chair s.
# Return the chair number of the prisoner who gets the last (bad-tasting) candy

def saveThePrisoner(n, m, s):
    return ((s + m - 2) % n) + 1







