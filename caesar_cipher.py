# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-three
#!/bin/python3

import math
import os
import random

import re
import sys

def caesarCipher(s, k):
    k = k%26
    result = ""
    for cha in s:
        if cha.isalpha():
            ascii_value_of_a = ord(cha)
            ascii_value_of_c = ascii_value_of_a + k
            if 97 <= ascii_value_of_a and ascii_value_of_a <= 122 and 122 < ascii_value_of_a + k:
                print((ascii_value_of_a%123, k%26, ascii_value_of_a, k))
                ascii_value_of_c = ((ascii_value_of_a%123)+k)%123 + 97
            elif 65 <= ascii_value_of_a and ascii_value_of_a <= 90 and 90 < ascii_value_of_a + k:
                ascii_value_of_c = ((ascii_value_of_a%91)+k)%91 +65
            result += chr(ascii_value_of_c)
        else:
            result += cha
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
