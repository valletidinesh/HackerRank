#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    days = [2]
    liked = [2]
    for i in range(1,n + 1):
        like = ((liked[i-1])*3)//2
        days.append( like + days[i-1])
        liked.append(like)
    return days[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
