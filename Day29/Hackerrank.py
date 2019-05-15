#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    comb=list(combinations(list(range(n)),2))
    NoOf=0
   
    for i in comb:
        
        if (i[1]>i[0]) and ((ar[i[0]]+ar[i[1]])%k==0):
            NoOf+=1
    return NoOf


if __name__ == '__main__':
    

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)