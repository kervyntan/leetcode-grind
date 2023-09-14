#!/bin/python3
#https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    # +ve
    positive = 0
    negative = 0
    neutral = 0
    length = len(arr)
    for num in arr:
        if (num > 0):
            positive+=1
        elif (num < 0):
            negative+= 1
        else:
            neutral+=1
            
    print("{:.6f}".format(positive / length))
    print("{:.6f}".format(negative / length))
    print("{:.6f}".format(neutral / length))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
