def solution(numbers, target):
    answer = 0
    def cal(idx, result):
        nonlocal answer
        if idx == len(numbers):
            if result == target:
                answer += 1
            return result
        cal(idx+1, result+numbers[idx])
        cal(idx+1, result+numbers[idx]*-1)
    cal(0,0)
    return answer

# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)

# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])