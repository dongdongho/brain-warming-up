# https://school.programmers.co.kr/learn/courses/30/lessons/12906

import re
def solution(arr):
    return [int(f) for f in re.sub(r'(.)\1*', r'\1', "".join(map(str, arr)))]
