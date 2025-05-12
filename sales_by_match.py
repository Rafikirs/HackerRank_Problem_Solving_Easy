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
