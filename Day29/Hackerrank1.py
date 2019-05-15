#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    setarr=set(arr)
    dictarr=dict(zip(setarr,[0 for i in setarr]))
    for i in arr:
        dictarr[i]+=1
    modearr=max(dictarr.values())
    modenum=[i for i in dictarr.keys() if dictarr[i]==modearr]
    return min(modenum)
    

if __name__ == '__main__':
    

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)