# Exercise: Lisa's workbook
# URL: https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true
# Description: Count how many problems have the same number as their page

def workbook(n, k, arr):
    page_count = 0
    special_count = 0
    for num in arr:
        for i in range(math.ceil(num / k)):
            page_count += 1
            if page_count in range(i*k+1, min((i+1)*k, num)+1):
                special_count += 1
    return special_count
