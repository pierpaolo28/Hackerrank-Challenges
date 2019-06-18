# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    res = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            res += 1
            i+=2
        else:
            i+=1
    return res

# Shorter solution
def sockMerchant(n, ar):
    return sum(map(lambda x: x//2, Counter(ar).values()))