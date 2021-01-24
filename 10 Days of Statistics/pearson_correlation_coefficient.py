n = int(input())
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

m1, m2 = sum(x)/n, sum(y)/n


def sd(arr, mean, n):
    num = []
    for i in arr:
        num.append((i-mean)**2)
    return (sum(num)/n)**(1/2)


sd1, sd2 = sd(x, m1, n), sd(y, m2, n)

num = []
for i, j in zip(x, y):
    num.append((i - m1)*(j - m2))

p = sum(num)/(n*sd1*sd2)
print(p)
