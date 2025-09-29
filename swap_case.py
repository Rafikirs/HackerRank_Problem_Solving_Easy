# Exercise: sWAP cASE
# URL: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# Description: Swap cases of a string

def swap_case(s):
    swapped_s = ""
    for char in s:
        if char.isupper() == False and char.islower() == False:
            swapped_s += char
        elif char.isupper():
            swapped_s += char.lower()
        else:
            swapped_s += char.upper()
            
    return swapped_s
