#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
l=[]
l1=[]
def sockMerchant(n, ar):
    s=0
    for j in ar:
        if j not in l1:
            l1.append(j)
    for b in l1:
        c=ar.count(b)
        l.append(c)
    for a in l:
        s+=(a%2)
    r=n-s
    return r//2
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
