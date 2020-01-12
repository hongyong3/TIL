import sys
sys.stdin = open("D4_1258_input.txt", "r")

# def dfs(x, y):
#     global count
#     i, j = 0, 0
#     while data[x + i][y]:
#         while data[x + i][y + i]:
#             j += 1
#             if y + j == N:
#                 break
#         i += 1
#         if x + i == N:
#             break
#     ans.append((i, j))
#     count += 1
#
#
# T = int(input())
# for test_case in range(2):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     count = 0
#     ans = []
#
#     for i in range(N):
#         for j in range(N):
#             if data[i][j]:
#                 dfs(i, j)
#     sorted(ans)
#     print("#{} {}".format(test_case + 1, count), end = " ")
#     for i in ans:
#         print(i[0], i[1], end= " ")
#     print()

# def row(x, y):
#     subCount = 0
#     while data[x][y + subCount]:
#         subCount += 1
#         if y + subCount == N:
#             break
#     return subCount
#
# def col(x, y):
#     subCount = 0
#     while data[x + subCount][y]:
#         subCount += 1
#         if x + subCount == N:
#             break
#     return subCount
#
# def reset(i, j, r, c):
#     for x in range(c):
#         for y in range(r):
#             data[i + x][j + y] = 0
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     count = 0
#     ans = []
#
#     for i in range(N):
#         for j in range(N):
#             if data[i][j]:
#                 r, c = row(i, j), col(i, j)
#                 reset(i, j, r, c)
#                 count += 1
#                 ans.append((r * c, c, r))
#     print("#{} {}".format(test_case + 1, count), *[str(i[1]) + ' ' + str(i[2]) for i in sorted(ans)])

def row(x, y):
    subCount = 0
    while data[x][y + subCount]:
        subCount += 1
        if y + subCount == N:
            break
    return subCount

def col(x, y):
    subCount = 0
    while data[x + subCount][y]:
        subCount += 1
        if x + subCount == N:
            break
    return subCount

def reset(i, j, r, c):
    for x in range(c):
        for y in range(r):
            data[i + x][j + y] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    ans = []

    for i in range(N):
        for j in range(N):
            if data[i][j]:
                r, c = row(i, j), col(i, j)
                reset(i, j, r, c)
                count += 1
                ans.append((r * c, c, r))
    print("#{} {}".format(test_case + 1, count), *[str(i[1]) + ' ' + str(i[2]) for i in sorted(ans)])