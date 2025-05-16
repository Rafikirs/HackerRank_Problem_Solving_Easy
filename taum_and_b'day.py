# Exercise: Taum and B'day
# URL: https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=true
# Description:
# Calculate the minimum cost to buy black and white gifts, considering the cost to convert between them

def taumBday(b, w, bc, wc, z):
    black_cost = min(bc, wc + z)
    white_cost = min(wc, bc + z)
    return b * black_cost + w * white_cost








