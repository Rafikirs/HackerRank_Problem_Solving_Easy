# Exercise: Find the Runner-Up Score!
# URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Description: Find the runner-up score in a list of n scores

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    print(list(set(arr))[1])
