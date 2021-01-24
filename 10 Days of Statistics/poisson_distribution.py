# 1
from math import factorial, exp

m = float(input())
x = int(input())

poisson_prob = ((m**x)*exp(-m))/factorial(x)
print(poisson_prob)

# 2
average_x, average_y = [float(i) for i in input().split(" ")]
cost_x = 160 + 40*(average_x + average_x**2)
cost_y = 128 + 40*(average_y + average_y**2)

print(cost_x)
print(cost_y)
