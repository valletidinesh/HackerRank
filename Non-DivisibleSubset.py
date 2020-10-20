#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(K, arr):
    # Write your code here
    f = [0]*K
    N = len(s)
    for i in range(N): 
        f[arr[i] % K] += 1 
    if (K % 2 == 0): 
        f[K//2] = min(f[K//2], 1)
    res = min(f[0], 1)
    for i in range(1,(K // 2) + 1): 
        res += max(f[i], f[K - i]) 
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
