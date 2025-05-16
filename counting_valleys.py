# Exercise: Counting Valleys
# URL: https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
# Description:
# A valley is a sequence below sea level that starts with a descent and ends when returning to sea level. 
# Count how many valleys are crossed during a hike

def countingValleys(steps, path):
    altitude = 0
    valleys = 0

    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1
        else:  
            altitude -= 1

    return valleys
