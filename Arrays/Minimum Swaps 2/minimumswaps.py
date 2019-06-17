# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    res = 0

    for i in range(0, len(arr) - 1):
        while arr[i] != i + 1:
            tmp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = tmp
            res += 1

    return res