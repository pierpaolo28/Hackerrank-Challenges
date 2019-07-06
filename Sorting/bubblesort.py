# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    count = 0
    for i in range(0, n):
        for j in range(0, n - 1):
        # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                count +=1
    print("Array is sorted in", count, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])
    return