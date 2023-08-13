# https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    arr = [[0]*(i+1) for i in range(n)]
    value, x, y = 1, -1, 0
    for i in range(n):
        for _ in range(n-i):
            if i%3 == 0:
                x += 1
            elif i%3 == 1:
                y += 1
            elif i%3 == 2:
                x -= 1
                y -= 1
            arr[x][y] = value
            value += 1
    return [num for sublist in arr for num in sublist]

# from itertools import chain
# def solution(n):
#     [row, col, cnt] = [-1, 0, 1]
#     board = [[None] * i for i in range(1, n+1)]
#     for i in range(n):
#         for _ in range(n-i):
#             if i % 3 == 0:
#                 row += 1
#             elif i % 3 == 1:
#                 col += 1
#             else:
#                 row -= 1
#                 col -= 1
#             board[row][col] = cnt
#             cnt += 1
#     return list(chain(*board)) # or  sum(nested_array, [])
