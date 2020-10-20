#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    c = s.count('a')
    if len(s) == c:
        return n
    if n >= len(s):
        count = (n // len(s))*c
        rem = n % len(s)
        for i in range(rem):
            if s[i] == 'a':
                count += 1
    else:
        count = 0
        for i in range(n):
            if s[i] == 'a':
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
