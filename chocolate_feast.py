# Exercise: Chocolate Feast
# URL: https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=true
# Description: Buying chocolate bars as long as we have enough wrappers obtained from the previous bars

def chocolateFeast(n, c, m):
    total_bars = n // c
    wrappers = total_bars

    while wrappers // m > 0:
        new_bars = wrappers // m
        wrappers = new_bars + wrappers % m 
        total_bars += new_bars
        
    return total_bars
        
