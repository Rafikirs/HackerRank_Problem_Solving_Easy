# Exercise: Drawing Book
# URL: https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
# Description: 
# Calculate the minimum number of page turns required to reach page p 
# from either the front or the back of a book with n pages.

def pageCount(n, p):
    from_front = p // 2
    from_back = (n // 2) - (p // 2)
  
    return min(from_front, from_back)
