def diagonalDifference(arr):
    n = len(arr)
    first_diag = sum(arr[i][i] for i in range(n))
    second_diag = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)
