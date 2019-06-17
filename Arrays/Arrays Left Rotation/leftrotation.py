# Complete the rotLeft function below.
def rotLeft(a, d):

    # Method 1 (inefficient running time)
    # for i in range(0, d):
    #     first = a[0];

    #     for j in range(0, len(a)-1):
    #         #Shift element of array by one
    #         a[j] = a[j+1];

    #     #First element of array is added to the end
    #     a[len(a)-1] = first;

    # Method 2
    # for i in range(0, d):
    #     removed = a.pop(0)
    #     a.append(removed)

    # Method 3
    a = a[d:] + a[:d]

    return a