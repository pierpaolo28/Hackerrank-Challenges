from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if ((Counter(note) - Counter(magazine)) == {}) == True:
        print('Yes')
    else:
        print('No')