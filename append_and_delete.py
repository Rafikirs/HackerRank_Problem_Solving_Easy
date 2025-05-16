# Exercise: Append and Delete
# URL: https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
# Description:
# Determine if it's possible to convert string s into string t by exactly k operations, 
# where each operation is either appending a character or deleting the last character

def appendAndDelete(s, t, k):
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    total_ops = (len(s) - common_length) + (len(t) - common_length)

    if total_ops > k:
        return "No"
    elif total_ops == k:
        return "Yes"
    elif (k - total_ops) % 2 == 0:
        return "Yes"
    elif k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"









