import sys
sys.stdin = open("D4_1210_input.txt", "r")

# 이전 풀이
# dx = [0, 0, - 1]
# dy = [- 1, 1, 0]
# def check(x, y):
#     if not (0 <= x < 100 and 0 <= y < 100) or data[x][y] == 0 or data[x][y]  == 9:
#         return False
#     return True
#
# def dfs(x, y):
#     while True:
#         if x == 0:
#             return y
#         for i in range(3):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if check(nx, ny):
#                 x = nx
#                 y = ny
#                 data[nx][ny] = 9
#
# for test_case in range(10):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(100)]
#     for i in range(99, - 1, - 1):
#         for j in range(99, - 1, - 1):
#             if data[i][j] == 2:
#                 print("#{} {}".format(test_case + 1, dfs(i, j)))
#                 break

def check(x, y):
    if 0 <= y < 100 and data[x][y] == 1:
        return True

def dfs(x, y):
    while True:
        if x == 0:
            return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny):
                data[x][y] = 9
                x, y = nx, ny

dx = [0, 0, - 1]
dy = [- 1, 1, 0]
for test_case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if data[99][i] == 2:
            print("#{} {}".format(test_case + 1, dfs(99, i)))
            break