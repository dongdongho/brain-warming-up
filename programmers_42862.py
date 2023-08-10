# https://school.programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    p_n = n - len(lost)
    lost = sorted(lost)
    
    # 1. 자급자족 학생들 추출
    self_serving = [lost_student for lost_student in lost if lost_student in reserve]
    p_n += len(self_serving)
    
    # 2. 자급자족 후 남은 학생과 체육복
    lost_students = [student for student in lost if student not in self_serving]
    reserve_cloths = [cloth for cloth in reserve if cloth not in self_serving]
    
    for item in lost_students:
        before = item - 1
        after = item + 1
        if before in reserve_cloths:
            p_n += 1
            reserve_cloths.remove(before)
        elif after in reserve_cloths:
            p_n += 1
            reserve_cloths.remove(after)
    return p_n