# Exercise: Electronics Shop
# URL: https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
# Description:
# A person wants to determine the most expensive computer keyboard and USB drive 
# that can be purchased with a give budget. Given price lists for keyboards and USB drives 
# and a budget, find the cost to buy them. If it is not possible to buy both items, return -1

def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b:
                max_spent = max(max_spent, total)
    return max_spent
