# Exercise: Cavity Map
# URL: https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true
# Description: When an element of a grid is higher than elements around, turn it into X

def cavityMap(grid):
    if len(grid) <= 2:
        return grid
    
    grid = [list(row) for row in grid]    
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            if (
                grid[i][j] > grid[i-1][j] and 
                grid[i][j] > grid[i+1][j] and
                grid[i][j] > grid[i][j-1] and 
                grid[i][j] > grid[i][j+1]
            ):
                grid[i][j] = "X"
    return ["".join(row) for row in grid]
