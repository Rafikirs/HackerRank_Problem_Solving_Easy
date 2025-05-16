# Exercise: Cats and a Mouse
# URL: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
# Description: 
# Two cats and a mouse are positioned on a line. Given their starting positions, 
# determine which cat reaches the mouse first. If both cats arrive simultaneously, 
# the mouse escapes. Return "Cat A", "Cat B", or "Mouse C" accordingly

def catAndMouse(x, y, z):
    dist_a = abs(x - z)
    dist_b = abs(y - z)
    
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"
