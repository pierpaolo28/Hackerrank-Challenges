x, y = [], []
for _ in range(5):
    i, j = list(map(float, input().split(" ")))
    x.append(i)
    y.append(j)

n = len(x)
xm = sum(x)/n
ym = sum(y)/n
x2 = sum([i**2 for i in x])
xy = sum([i*j for i, j in zip(x, y)])

b = (n*xy - sum(x)*sum(y))/(n*x2 - sum(x)**2)
a = ym - b*xm

yhat = a + b*80
print(yhat)
