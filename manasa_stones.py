# Exercise: Manasa Stones
# URL: https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true
# Description: Find all possible arrival points based on 2 possible step lengths

def stones(n, a, b):
    results = set()
    for i in range(n):
        results.add(i*a + (n-1-i)*b)
    return sorted(results)
