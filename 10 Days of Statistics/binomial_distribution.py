# 1
l, r = list(map(float, input().split(" ")))
odds = l / r


def fact(n):
    return 1 if n == 0 else n*fact(n-1)


def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))


def binomial(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)


print(sum([binomial(i, 6, odds / (1 + odds)) for i in range(3, 7)]))


# 2
p, n = list(map(int, input().split(" ")))

print(sum([binomial(i, n, p/100) for i in range(3)]))
print(sum([binomial(i, n, p/100) for i in range(2, n+1)]))
