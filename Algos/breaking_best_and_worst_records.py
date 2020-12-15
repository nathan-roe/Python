#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    maxc = 0
    minc = 0
    for score in scores:
        if score > max:
            max = score
            maxc += 1
        if score < min:
            min = score
            minc += 1
    return maxc, minc
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()