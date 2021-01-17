n = int(input())
arr = sorted([int(i) for i in input().split()])

print(round(sum(arr)/n, 1))
if n%2==0:
    print(round((arr[n//2-1]+arr[n//2])/2, 1))
else:
    print(round(arr[n//2], 1))
    
dic = {}
for i in arr:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

res = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        
if list(res.values())[0] == 1:
    print(arr[0])
else:
    print(list(res.keys())[0])