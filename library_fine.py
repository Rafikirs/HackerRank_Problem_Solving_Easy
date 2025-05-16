# Exercise: Library Fine
# URL: https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true
# Description: 
# Calculate the library fine based on how late the book is returned compared to 
# its due date, applying fines according to year, month, or day lateness

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    if y1 > y2:
        return 10000
    if m1 > m2:
        return 500 * (m1 - m2)
    return 15 * (d1 - d2)









