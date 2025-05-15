def angryProfessor(k, a):
    on_time = sum(1 for time in a if time <= 0)
    return "NO" if on_time >= k else "YES"
