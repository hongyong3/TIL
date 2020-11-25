import sys
sys.stdin = open("D4_1494_input.txt", "r")
from itertools import combinations

# def solve(i, j):
#     global answer
#     if i == len(a) // 2:
#         return
#     X, Y = 0, 0
#     for x in range(N // 2):
#         if (a[i][x][0] >= 0 and a[j][x][0] >= 0) or (a[i][x][0] < 0 and a[j][x][0] < 0):
#             X += a[i][x][0] + a[j][x][0]
#         else:
#             X += a[i][x][0] - a[j][x][0]
#
#         if (a[i][x][1] >= 0 and a[j][x][1] >= 0) or (a[i][x][1] < 0 and a[j][x][1] < 0):
#             Y += a[i][x][1] + a[j][x][1]
#         else:
#             Y += a[i][x][1] - a[j][x][1]
#     ans = X * X + Y * Y
#     if answer >= ans:
#         answer = ans
#     solve(i + 1, j - 1)
#
# T = int(input())
# for test_case in range(2):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     a = list(combinations(data, N // 2))
#     answer = float('inf')
#     solve(0, - 1)
#     print("#{} {}".format(test_case + 1, answer))

# def solve(n, count):
#     global answer
#     if count == N // 2:
#         x, y = 0, 0
#         for i in range(N):
#             if check[i] == 1:
#                 x += data[i][0]
#                 y += data[i][1]
#             else:
#                 x -= data[i][0]
#                 y -= data[i][1]
#         if answer > x * x + y * y:
#             answer = x * x + y * y
#         return
#     for i in range(n, N):
#         if check[i] == 0:
#             check[i] = 1
#             solve(i + 1, count + 1)
#             check[i] = 0
#
# T = int(input())
# for test_case in range(2):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     answer = float('inf')
#     check = [0] * 20
#     solve(0, 0)
#     print("#{} {}".format(test_case + 1, answer))

# 가지치기 추가
case = [0, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310, 92378]

def solve(n, cnt):
    global ans, c
    if not c or not ans:
        return
    if cnt == N // 2:
        c -= 1
        x, y = 0, 0
        for i in range(N):
            if chk[i]:
                x += data[i][0]
                y += data[i][1]
            else:
                x -= data[i][0]
                y -= data[i][1]
        if ans > x * x + y * y:
            ans = x * x + y * y
        return

    for i in range(n, N):
        if not chk[i]:
            chk[i] = 1
            solve(i + 1, cnt + 1)
            chk[i] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    chk = [0] * N
    c = case[N // 2]
    solve(0, 0)
    print("#{} {}".format(test_case + 1, ans))