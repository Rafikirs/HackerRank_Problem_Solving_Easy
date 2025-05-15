def hurdleRace(k, height):
    max_hurdle = max(height)
    return max(0, max_hurdle - k)
