n = int(input())
arr = sorted([int(i) for i in input().split()])

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

q2, l, r = median(arr, n)
q1, l2, r2 = median(l, len(l))
q3, l3, r3 = median(r, len(r))
print(q1)
print(q2)
print(q3)