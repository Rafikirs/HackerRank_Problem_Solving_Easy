# Exercise: Service Lane
# URL: https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true
# Description: Calculate the maximum size vehicle that can travel that segment of a service lane

def serviceLane(n, cases):
    results = []
    for i, j in cases:
        results.append(min(width[i:j+1]))
    return results
