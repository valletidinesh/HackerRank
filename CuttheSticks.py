#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = [len(arr)]
    while len(arr):
        m = min(arr)
        for i in range(len(arr)):
            arr[i] = arr[i] - m
        for i in range(len(arr)):
            if (0 in arr):
                arr.remove(0)
            else:
                break
        if len(arr) != 0:       
            result.append(len(arr))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
