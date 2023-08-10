# https://school.programmers.co.kr/learn/courses/30/lessons/12909
from collections import deque
def solution(s):
    stat_q = deque()
    for item in s:
        if item == "(":
            stat_q.append("(")
        elif item == ")":
            if len(stat_q) == 0:
                return False
            stat_q.pop()
    if len(stat_q) != 0:
        return False
    return True
            


# def solution(numbers, target):

#     def calc(idx, sum):
#         nonlocal answer

#         if idx == len(numbers):
#             if sum == target:
#                 answer += 1
#             return

#         calc(idx+1, sum + numbers[idx])
#         calc(idx+1, sum - numbers[idx])

#     answer = 0
#     calc(0, 0)

#     return answer

# from collections import defaultdict as dd
# def solution(numbers, target):
#     a = [0]
#     d = dd(int)
#     d[0] = 1
#     for n in numbers:
#         nd = dd(int)
#         na = []
#         for i in a:
#             if i+n not in nd:
#                 na.append(i+n)
#             if i-n not in nd:
#                 na.append(i-n)
#             nd[i+n] += d[i]
#             nd[i-n] += d[i]
#         d = nd
#         a = na
#     return d[target]
