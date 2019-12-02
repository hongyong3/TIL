import sys
sys.stdin = open("D4_1861_input.txt", "r")


# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def dfs(x, y, n):
#     global count, ans, number
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not (0 <= nx < N and 0 <= ny < N):
#             continue
#         if data[nx][ny] == data[x][y] + 1:
#             count += 1
#             dfs(nx, ny, n)
#             count -= 1
#
#     if count >= ans:
#         ans = count
#         if n <= number:
#             number = n
#         return
#
# T = int(input())
# for test_case in range(2):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans, number = 0, float('inf')
#     for x in range(N):
#         for y in range(N):
#             count = 1
#             dfs(x, y, data[x][y])
#     print("#{} {} {}".format(test_case + 1, number, ans))

##########################################################################################


# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
#
# def dfs(x, y, n):
#     global count, ans, number
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not (0 <= nx < N and 0 <= ny < N):
#             continue
#         if data[nx][ny] == data[x][y] + 1:
#             count += 1
#             dfs(nx, ny, n)
#             count -= 1
#
#     if count >= ans:
#         ans = count
#         if n <= number:
#             number = n
#
#
# N = 3
# # data = [[9, 3, 4], [6, 1, 5], [7, 8, 2]]
# data = [[1, 2, 3], [2, 4, 5], [3, 4, 5]]
# data = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# ans, number = 0, float('inf')
# for x in range(N):
#     for y in range(N):
#         count = 1
#         tt = data[x][y]
#         dfs(x, y, data[x][y])

###############################################################################


# def solve(q):
#     global ans, number
#     while q:
#         x, y, n = q.pop()
#         if ans < n:
#             ans = n
#             number = data[x][y]
#         if ans == n:
#             number = min(number, data[x][y])
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if not (0 <= nx < N and 0 <= ny < N):
#                 continue
#             if data[nx][ny] == data[x][y] + 1:
#                 q.append((nx, ny, n + 1))
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     q, ans, number =[], 0, float('inf')
#     for x in range(N):
#         for y in range(N):
#             q.append((x, y, 1))
#             solve(q)
#     print("#{} {} {}".format(test_case + 1, number, ans))


########################################################################################


# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     # q, ans, number = [], 0, float('inf')
#     q = []
#     ans = 0
#     number = float('inf')
#     for i in range(N):
#         for j in range(N):
#             q.append((i, j, 1))
#             while q:
#                 x, y, n = q.pop()
#                 if ans < n:
#                     ans = n
#                     if number > data[x][y]:
#                         number = data[x][y]
#                 if ans == n:
#                     number = min(number, data[x][y])
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if not (0 <= nx < N and 0 <= ny < N):
#                         continue
#                     if data[nx][ny] == data[x][y] + 1:
#                         q.append((nx, ny, n + 1))
#     print("#{} {} {}".format(test_case + 1, number, ans))


##############################################################################

def dfs(x, y, n):
    global count, ans, number
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if data[nx][ny] == data[x][y] + 1:
            count += 1
            dfs(nx, ny, n)
            count -= 1

    if count >= ans:
        ans = count
        if n <= number:
            number = n
        return

T = int(input())
for test_case in range(2):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, number = 0, float('inf')
    for x in range(N):
        for y in range(N):
            count = 1
            dfs(x, y, data[x][y])
    print("#{} {} {}".format(test_case + 1, number, ans))
dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def dfs(x, y, n):
    global count, ans, number
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if data[nx][ny] == data[x][y] + 1:
            count += 1
            dfs(nx, ny, n)
            count -= 1

    if count >= ans:
        ans = count
        number = min(number, n)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, number = 0, float('inf')
    for x in range(N):
        for y in range(N):
            count = 1
            dfs(x, y, data[x][y])
    print("#{} {} {}".format(test_case + 1, number, ans))