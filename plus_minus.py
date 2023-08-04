# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-one
#!/bin/python3

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
    num_plus = len([f for f in arr if f > 0])
    num_minus = len([f for f in arr if f < 0])
    num_zero = len([f for f in arr if f == 0])
    print(f"{num_plus/(num_plus+num_minus+num_zero):.6}")
    print(f"{num_minus/(num_plus+num_minus+num_zero):.6}")
    print(f"{num_zero/(num_plus+num_minus+num_zero):.6}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

