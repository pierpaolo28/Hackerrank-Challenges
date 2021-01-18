n = int(input())
arr = sorted([int(i) for i in input().split()])

mean = sum(arr)/n

num = []
for i in arr:
    num.append((i-mean)**2)
    
sigma = round((sum(num)/n)**(1/2), 1)
print(sigma)