#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):

    # Method 1 (inefficient running time)
    # for i in range(0, d):
    #     first = a[0];

    #     for j in range(0, len(a)-1):
    #         #Shift element of array by one
    #         a[j] = a[j+1];

    #     #First element of array is added to the end
    #     a[len(a)-1] = first;

    # Method 2
    # for i in range(0, d):
    #     removed = a.pop(0)
    #     a.append(removed)

    # Method 3
    a = a[d:] + a[:d]

    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()