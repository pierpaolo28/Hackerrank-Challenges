# Complete the countingValleys function below.
def countingValleys(n, s):
    u = 0
    d = 0
    count = 0
    for i in s:
        if i == "U":
            u += 1
            if u-d == 0:
                count += 1
        else:
            d += 1
    return count
