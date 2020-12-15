#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a_min = a[0]
    b_max = b[0]
    count = 0
    for mina in a:
        if mina < a_min:
            a_min = mina
    for maxb in b:
        if maxb > b_max:
            b_max = maxb
    bool_boy = False
    for i in range(a_min, b_max + 1):
        for b_val in b:
            if b_val % i != 0:
                bool_boy = True
                break
        for a_val in a:
            if i % a_val != 0:
                bool_boy = True
                break
        if bool_boy:
            bool_boy = not bool_boy
        else:
            count += 1
    print(count)
    return count
        
                
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()