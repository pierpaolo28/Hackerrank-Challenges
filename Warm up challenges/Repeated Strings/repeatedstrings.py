# Complete the repeatedString function below.
def repeatedString(s, n):

    # Most time efficient method
    k = s.count("a")*(n/len(s))
    k += s[:n%len(s)].count("a")
    return int(k)

    # Alternative method 1
    # res = 0
    # while len(s) < n:
    #     s += s
        # if len(s) >= n:
            # for i in s[0:n]:
            #         if i == 'a':
            #             res += 1
    # return res

    # Alternative method 2
    # res = 0
    # s = (s * (n//len(s) + 1))[:n]
    # res = s.count('a')
    # return res
