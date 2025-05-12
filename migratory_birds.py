def migratoryBirds(arr):
    bird_count = {}
    
    for bird in arr:
        if bird in bird_count:
            bird_count[bird] += 1
        else:
            bird_count[bird] = 1
    
    max_count = max(bird_count.values())
    
    most_frequent_birds = [bird for bird, count in bird_count.items() if count == max_count]
    
    return min(most_frequent_birds)
