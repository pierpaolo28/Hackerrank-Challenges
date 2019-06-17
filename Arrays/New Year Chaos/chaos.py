# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for ind, val in enumerate(q):
        if val-1 - ind > 2:
            return print("Too chaotic")
        for j in range(max(0,val-2), ind):
            if q[j] > val:
                bribes+=1
    return print(bribes)
