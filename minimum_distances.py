# Exercise: Minimum Distances
# URL: https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true
# Description: Given an array, find the minimum distance between any pair of equal elements

def minimumDistances(a):
  index_dict = {}
    for i, n in enumerate(a):
        if n in index_dict:
          index_dict[n].append(i)
        else:
            index_dict[n] = [i]

    distances = [
        j - i
        for indices in index_dict.values() if len(indices) > 1
        for i, j in zip(indices, indices[1:])
    ]

    return min(distances) if distances else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
