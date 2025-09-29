# Exercise: Python Lists
# URL: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Description: Perform a series of specific operations on a list

if __name__ == '__main__':
    N = int(input())
    init = []
    operations = [input() for _ in range(N)]
    for operation in operations:
        if operation.split()[0] == "insert":
            init.insert(int(operation.split()[1]), int(operation.split()[2]))
        elif operation == "print":
            print(init)
        elif operation.split()[0] == "append":
            init.append(int(operation.split()[1]))
        elif operation.split()[0] == "remove":
            init.remove(int(operation.split()[1]))
        elif operation == "sort":
            init.sort()
        elif operation == "pop":
            init.pop()
        elif operation == "reverse":
            init.reverse()
