#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def get_median(counts, mids):
    res = []
    for mid in mids:
        gone = 0
        for i, v in enumerate(counts):
            gone += v
            if gone >= mid:
                res.append(i)
                break
    return sum(res) / len(res)


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    # Using counting sort (Max lenght of expenditure = 200)
    counts = [0] * 201

    # Finding the indeces of the median values
    if d % 2 == 0:
        mid = [d // 2, d // 2 + 1]
    else:
        mid = [d // 2 + 1]

    for j in expenditure[:d]:
        # Adding elements to counting sort
        counts[j] += 1

    # Calculating trailing days median and notification count
    for i, exp in enumerate(expenditure[d:]):
        median = get_median(counts, mid)

        if exp >= 2 * median:
            notifications += 1

        # Deleting the oldest value and adding the next entry
        old_value = expenditure[i]
        counts[old_value] -= 1
        counts[exp] += 1

    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
