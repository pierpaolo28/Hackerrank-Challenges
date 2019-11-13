import numpy as np
from itertools import permutations

s = 'xacxzaa'
b = 'fxaazxacaaxzoecazxaxaz'

s = list(s)
# b = list(b)

perm_s = permutations(s)
perm_s_list = []
for i in list(perm_s):
    perm_s_list.append(''.join(i))

print(len(perm_s_list))

it = []
for i in perm_s_list:
    if b.find(str(i)) != 1:
        it.append(i)

#print(count)
print(len(set(it)))
