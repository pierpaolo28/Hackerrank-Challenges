# 1
a, b = list(map(int, input().split(" ")))
n = int(input())

p = a/b
q = 1-p
g = q**(n-1)*p

print(g)

# 2
a, b = list(map(int, input().split(" ")))
n = int(input())

p = a/b
q = 1-p
prob = 1 - q**n

print(prob)
