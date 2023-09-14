#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    
    min = 0
    max = 0
    for index, val in enumerate(arr):
        if index == 0:
            min += val
        elif index == len(arr) - 1:
            max += val
        else:
            min += val
            max += val
            
    print("{x:} {y:}".format(x = min, y = max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
