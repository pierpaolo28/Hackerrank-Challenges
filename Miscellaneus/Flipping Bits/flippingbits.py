# Complete the flippingBits function below.
def flippingBits(n):
    n = "{0:32b}".format(n)
    ib_string = ""

    for bit in n:
        if bit == "1":
            ib_string += "0"
        else:
            ib_string += "1"
    n = int(ib_string, 2)
    return n
