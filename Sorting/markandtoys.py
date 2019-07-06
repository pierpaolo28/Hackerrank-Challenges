# Complete the maximumToys function below.
def maximumToys(prices, k):
    # n = len(prices)
    maxspend = 0
    objcount = 0
    # Bubble sort implementation alternative (less time efficient)
    # for i in range(0, n):
    #     for j in range(0, n - 1):
    #     # Swap adjacent elements if they are in decreasing order
    #         if (prices[j] > prices[j+1]):
    #             tmp = prices[j]
    #             prices[j] = prices[j+1]
    #             prices[j+1] = tmp
    prices.sort()
    for w in prices:
        if w + maxspend < k:
            maxspend += w
            objcount += 1
        else:
            break
    return objcount