n = input()
arr = [int(i) for i in input().split()]
weights = [int(i) for i in input().split()]

num = []
for i, j in zip(arr, weights):
    num.append(i*j)

print(round(sum(num)/sum(weights),1))