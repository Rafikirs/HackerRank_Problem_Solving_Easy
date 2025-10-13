# Exercise: Number Line Jumps
# URL: http://hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# Description: Create a simple mathematical function which prints YES if the problem has a solution

def kangaroo(x1, v1, x2, v2):
    if v2 != v1:
        n = (x1-x2)/(v2-v1)
        if n.is_integer() and n > 0:
            return  "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
