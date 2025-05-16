# Exercise: Utopian Tree
# URL: https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
# Description: 
# Simulate the growth of a Utopian Tree that doubles in height each spring and increases 
# by 1 meter each summer, starting at 1 meter. Return the tree's height after n growth cycles

def utopianTree(n):
    height = 1
    for cycle in range(n):
        if cycle % 2 == 0:
            height *= 2
        else:
            height += 1
    return height
