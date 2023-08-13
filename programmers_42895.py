# https://school.programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    # dp[i]는 숫자 N을 i번 사용하여 만들 수 있는 모든 수의 집합
    dp = [set() for _ in range(9)]

    # 각 i에 대해 N을 i번 사용한 경우 초기화
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

    # 다이나믹 프로그래밍을 통해 각 경우의 수 계산
    for i in range(1, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                # print(dp)
        if number in dp[i]:
            return i

    return -1  # N 사용 횟수로 만들 수 없는 경우

# def solution(N, number):
#     S = [{N}]
#     for i in range(2, 9):
#         lst = [int(str(N)*i)]
#         for X_i in range(0, int(i / 2)):
#             for x in S[X_i]:
#                 for y in S[i - X_i - 2]:
#                     lst.append(x + y)
#                     lst.append(x - y)
#                     lst.append(y - x)
#                     lst.append(x * y)
#                     if x != 0: lst.append(y // x)
#                     if y != 0: lst.append(x // y)
#         if number in set(lst):
#             return i
#         S.append(lst)
#     return -1