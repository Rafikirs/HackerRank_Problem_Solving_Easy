def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b:
                max_spent = max(max_spent, total)
    return max_spent
