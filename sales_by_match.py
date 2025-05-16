# Exercise: Sales by Match
# URL: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
# Description:
# There is a large pile of socks that must be paired by color. Given an array of integers 
# representing the color of each sock, determine how many pairs of socks with matching colors there are

def sockMerchant(n, ar):
    sock_count = {}
    pairs = 0
    
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1
    
    for count in sock_count.values():
        pairs += count // 2  
    
    return pairs
