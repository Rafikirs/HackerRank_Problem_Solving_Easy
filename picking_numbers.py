def pickingNumbers(a):
    max_len = 0
  
    for num in a:
        current = sum(1 for x in a if abs(x - num) <= 1)
        max_len = max(max_len, current)

    return max_len
