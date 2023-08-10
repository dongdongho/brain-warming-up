# https://school.programmers.co.kr/learn/courses/30/lessons/42840#
from collections import Counter
def solution(answers):
    cnt = Counter({1:0, 2:0, 3:0})
    f_pattern = [1,2,3,4,5]
    s_pattern = [2,1,2,3,2,4,2,5]
    t_pattern = [3,3,1,1,2,2,4,4,5,5]
    for idx, answer in enumerate(answers):
        if answer == f_pattern[idx%len(f_pattern)]:
            cnt[1] += 1
        if answer == s_pattern[idx%len(s_pattern)]:
            cnt[2] += 1
        if answer == t_pattern[idx%len(t_pattern)]:
            cnt[3] += 1
    return [key for key, value in cnt.items() if value == cnt.most_common()[0][1]]