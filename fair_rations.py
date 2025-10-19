# Exercise: Fair Rations
# URL: https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true
# Description: Distributing the minimum number of bread loaves 

def fairRations(B):
    loaves = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1         
            B[i + 1] += 1     
            loaves += 2       

    if B[-1] % 2 != 0:
        return "NO"
    else:
        return str(loaves)
