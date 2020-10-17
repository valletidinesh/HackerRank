#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    divisor = []
    c = 0
    for i in list(str(n)):
        if int(i) in divisor:
            c += 1
        elif int(i) !=0  and n % int(i) == 0:
            c += 1
            divisor.append(int(i))
    return c
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
