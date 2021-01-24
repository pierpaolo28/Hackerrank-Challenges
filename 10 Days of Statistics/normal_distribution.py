import math

# 1
mean, std = 20, 2


def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(cdf(19.5))
print(cdf(22) - cdf(20))

# 2
mean, std = 70, 10

print((1-cdf(80))*100)
print((1-cdf(60))*100)
print((cdf(60))*100)
