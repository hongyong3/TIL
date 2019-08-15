# import sys
# sys.stdin = open("D2_1979_input.txt", "r")
# ​
# def DFS(x, y):
#     global count, ans
#     dx = [1, 0]
#     dy = [0, 1]
#     for i in range(2):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
# ​
#         if new_x < 0 or new_x == N: continue
#         if new_y < 0 or new_y == N: continue
#         if data[new_x][new_y] == 0: continue
#         if data[new_x][new_y] == 1:
#             count += 1
#             print(count)
# ​
#     if count == K:
#         ans += 1
#         count = 0
# ​
# ​
# ​
# T = int(input())
# for test_case in range(1):
#     count, ans = 0, 0
#     N, K = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == 1:
#                 # print(i, j)
#                 DFS(i, j)
#     # print("#{} {}".format(test_case + 1, ans))

import sys
sys.stdin = open("D2_1979_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data_row = [''.join(input().split()) for _ in range(N)]
    data_col = [''.join(i) for i in zip(*data_row)]
    total = data_row.copy()
    total.extend(data_col)
    ans = 0
    for i in total:
        result = i.split('0')
        if '1' * K in result:
            ans += result.count('1' * K)
    print("#{} {}".format(test_case + 1, ans))


# version 1
#
#
#
#
# def DFS(x, y):
#     dx = [1, 0]
#     dy = [0, 1]
#     for i in range(2):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#
#         if new_x < 0 or new_x >= N: continue
#         if new_y < 0 or new_y >= N: continue
#
#
#
# T = int(input())
# for test_case in range(1):
#     count, ans = 0, 0
#     N, K = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     for i in range(N):
#         count = 0
#         for j in range(N):
#             if data[i][j] == 1:
#                 count += 1
#                 while j + 1 < N:
#                     if count == K:
#                         if data[i][j+1] == 1:
#                             continue
#                         ans += 1
#                DFS(i, j)
#     print("#{} {}".format(test_case + 1, ans))
#