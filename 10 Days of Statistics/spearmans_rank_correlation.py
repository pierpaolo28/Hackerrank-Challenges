n = int(input())
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]
xs = sorted(x)
ys = sorted(y)

d2 = []
for i, j in zip(x, y):
    d2.append((xs.index(i) - ys.index(j))**2)

r = 1 - (6*sum(d2))/(n*(n**2 - 1))
print(r)
