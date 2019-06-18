# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*n
    res = 0
    itt = 0
    for i in queries:
        arr[i[0] - 1] = arr[i[0] - 1] + i[2]
        if i[1] != len(arr):
            arr[i[1]] = arr[i[1]] - i[2]
    for j in arr:
        itt = itt + j
        if itt > res:
            res = itt
    return res