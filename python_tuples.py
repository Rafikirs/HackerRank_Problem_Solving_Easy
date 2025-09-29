# Exercise: Python Tuples
# URL: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Description: Using hash function on a tuple

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

    t = tuple(integer_list)
    print(hash(t))
