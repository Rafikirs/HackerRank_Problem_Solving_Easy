# Exercise: Migratory Birds
# URL: https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
# Description: 
# Given an array of bird sightings where every element represents a bird type id, 
# determine the id of the most frequently sighted type. If more than 1 type has been spotted 
# that maximum amount, return the smallest of their ids.

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
