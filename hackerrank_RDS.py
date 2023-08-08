# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-four
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    cnt = 0
    while len(n) > 1:
        n = str(sum(map(int, n)))
        cnt += 1
    n = "".join([n for _ in range(k)])
    while len(n) > 1:
        n = str(sum(map(int, n)))
        cnt += 1
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

## Solutions
# def superDigit(n, k):
#     return (k * int(n)) % 9

# def superDigit(n, k):
#     sum=0
#     for i in n:
#         sum += int(i)*k
#     if sum<10:
#         return sum
#     return superDigit(str(sum), 1)