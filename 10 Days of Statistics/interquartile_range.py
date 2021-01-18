n = int(input())
a = [[int(i)]*int(j) for i, j in zip(input().split(), input().split())]
a = [j for i in a for j in i]
arr = sorted(a)

def median(a, le):
    if le%2 == 0:
        q = (a[le//2-1]+a[le//2])//2
        l = arr[:le//2]
        r = arr[le//2:]
    else:
        q = a[le//2]
        l = arr[:le//2]
        r = arr[le//2+1:]
    return q, l, r

q2, l, r = median(arr, len(arr))
q1, l2, r2 = median(l, len(l))
q3, l3, r3 = median(r, len(r))
res = float(q3 - q1)
print(round(res, 1))