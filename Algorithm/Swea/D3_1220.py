import sys
sys.stdin = open("D3_1220_input.txt", "r")

# def DFS(x, y):
#     nx = x
#     if data[x][y] == 1:
#         if x == N - 1:
#             data[x][y] = 0
#             return
#         nx += 1
#         if data[nx][y] == 0:
#             data[nx][y], data[x][y] = 1, 0
#             DFS(nx, y)
#         if data[nx][y] == (1 or 2):
#             return
#     else:
#         if x == 0:
#             data[x][y] = 0
#             return
#         nx -= 1
#         if data[nx][y] == 0:
#             data[nx][y], data[x][y] = 2, 0
#             DFS(nx, y)
#         if data[nx][y] == (1 or 2):
#             return
#
# def check(x, y):
#     global count
#     nx = x + 1
#     if nx < N:
#         if data[x][y] == 1 and data[nx][y] == 2:
#             data[x][y], data[nx][y] = 9, 9
#             count += 1
#         if data[x][y] == 2 and data[nx][y] == 1:
#             data[x][y], data[nx][y] = 9, 9
#             count += 1
#
# for test_case in range(10):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     count = 0
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == 1 or data[i][j] == 2:
#                 DFS(i, j)
#
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == 1 or data[i][j] == 2:
#                 check(i, j)
#
#     print("#{} {}".format(test_case + 1, count))

def solve(data):
    count = 0
    for x in range(N):
        flag = 0
        for y in range(N):
            if flag == 0 and data[y][x] == 1:
                flag = 1
            elif flag == 1 and data[y][x] == 2:
                count += 1
                flag = 0
    return count


for test_case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    print("#{} {}".format(test_case + 1, solve(data)))