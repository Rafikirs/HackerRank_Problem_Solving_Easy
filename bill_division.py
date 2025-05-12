def bonAppetit(bill, k, b):
    total_cost = sum(bill) - bill[k]
    anna_share = total_cost // 2
    
    if anna_share == b:
        print("Bon Appetit")
    else:
        print(b - anna_share)







