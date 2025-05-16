# Exercise: Bill Division
# URL: https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
# Description: 
# Determine if Brian fairly charged Anna for the shared meal, excluding the item she didn't eat. 
# Print "Bon Appetit" if the charge is correct, or the refund amount if she was overcharged.

def bonAppetit(bill, k, b):
    total_cost = sum(bill) - bill[k]
    anna_share = total_cost // 2
    
    if anna_share == b:
        print("Bon Appetit")
    else:
        print(b - anna_share)







