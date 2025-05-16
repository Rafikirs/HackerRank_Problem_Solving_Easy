# Exercise: The Hurdle Race
# URL: https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
# Description:
# Determine how many doses of a magic potion a character needs to jump over all hurdles in a race. 
# Each dose increases the jump height by 1. Return 0 if no potion is needed.

def hurdleRace(k, height):
    max_hurdle = max(height)
    return max(0, max_hurdle - k)
