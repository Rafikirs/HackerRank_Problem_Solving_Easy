# Exercise: Jumping on the clouds: revisited
# URL: http://hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
# Description: Jumping from one element of a list to another and changing a score depending on the landing point

def jumpingOnClouds(c, k):
    i = 0
    n = len(c)
    score = 100
    while True:
        i = (i+k)%n
        score -= 1
        if c[i] == 1:
            score -= 2
        if i == 0:
            break
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
