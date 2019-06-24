# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    res = 0
    while i < len(c)-1:
        if i+2 < len(c) and c[i+2] != 1:
            i += 1
        res += 1
        i += 1
    return res