# Exercise: Halloween Sale
# URL: https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true
# Description: Counting how many games can be bought given a price, a price decrease, a minimum price and a budget

def howManyGames(p, d, m, s):
    prices_sum = 0
    price = p
    games_count = 0
    
    while prices_sum + price <= s:
        games_count += 1
        prices_sum += price
        if price - d > m:
            price -= d
        else:
            price = m
            
    return games_count
