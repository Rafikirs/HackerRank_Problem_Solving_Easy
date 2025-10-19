# Exercise: Happy ladybugs
# URL: https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true
# Description: Finding if it's possible to permute an array to make ladybugs happy

from collections import Counter

def happyLadybugs(b):
    if len(b) < 2:
        if b == "_":
            return "YES"
        return "NO"
    if "_" not in b:
        match = (b[0] == b[1] and b[-2] == b[-1])
        for i in range(1, len(b)-1):
            match &= (b[i] == b[i-1] or  b[i] == b[i+1])
        
        if match == True:
            return "YES"
        return "NO"
    
    for color, count in Counter(b).items():
        if color != "_" and count == 1:
            return "NO"
    return "YES"
            
