#!/bin/python3

import math
import os
import random
import re
import sys


def appendAndDelete(s, t, k):
    if ((len(s) + len(t)) < k): 
        return 'Yes'
    n = min(len(s),len(t))
    i = 0
    while i<n:
        if s[i] != t[i]:
            break
        i += 1
    nOpe = len(s)+len(t) - 2 * i
    dOpe = k - nOpe
    if nOpe <= k  and dOpe % 2 == 0:
        return "Yes"
    return "No"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
