# Complete the primality function below.
def primality(n):
    # if n==1:
    #     return "Not prime"
    # for i in range(2,n-1):
    #     if n%i==0:
    #         return "Not prime"
    # return "Prime"
    if n==1:
        return "Not prime"
    # Loop till maximum the square root plus one of the number under examination
    # In this way we can improve time performances
    for i in range(2, int(n**0.5) +1):
        if n%i==0:
            return "Not prime"
    return "Prime"