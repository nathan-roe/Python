#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
#     s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
    # if apple is > s and < t retApp++  same with orange
    # a + apples = apples spot b + oranges = orange spot
    aCount = 0
    bCount = 0
    for apple in range(0, len(apples)):
        
        if apples[apple] + a >= s and apples[apple] + a <= t:
            aCount += 1
    for orange in range(0, len(oranges)):
        if oranges[orange] + b >= s and oranges[orange] + b <= t:
            bCount += 1
    print(aCount)
    print(bCount)
    
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)