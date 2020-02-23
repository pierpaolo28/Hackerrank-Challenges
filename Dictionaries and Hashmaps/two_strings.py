from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if (Counter(s2).keys() & Counter(s1)) != set():
        return 'YES'
    return 'NO'