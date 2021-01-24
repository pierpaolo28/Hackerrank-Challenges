import math

# 1
x, n = int(input()), int(input())
mu, sigma = float(input()), float(input())
mu_sum = n*mu
sigma_sum = math.sqrt(n)*sigma


def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))


print(cdf(x, mu_sum, sigma_sum))

# 2
x, n = int(input()), int(input())
mu, sigma = float(input()), float(input())
mu_sum = n*mu
sigma_sum = math.sqrt(n)*sigma

cdf = 0.5*(1 + math.erf((x - mu*n)/(sigma_sum*math.sqrt(2))))
print(cdf)

# 3
n, mu = float(input()), float(input())
sigma, interval = float(input()), float(input())
z = float(input())

sigma_n = sigma/(n**0.5)
print(mu - sigma_n*z)
print(mu + sigma_n*z)
