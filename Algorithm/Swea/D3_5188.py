import sys
sys.stdin = open("D3_5188_input.txt", "r")

# 이전 풀이
# def dfs(x, y, sum):
#     global min
#     ###########################
#     if min <= sum:          # 가지치기
#         return
#     #########################
#     if x == N-1 and y == N-1:
#         if min > sum:
#             min = sum
#     else:
#         if x + 1 < N:
#             dfs(x+1, y, sum + data[x+1][y])
#         if y + 1 < N:
#             dfs(x, y + 1, sum + data[x][y + 1])
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     min = 987654321
#     dfs(0, 0, data[0][0])    # x, y, sum
#
#     print("#{} {}".format(test_case + 1, min))

def dfs(x, y, total):
    global ans

    if ans <= total:
        return

    if x == y == N - 1:
        ans = total
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, total + data[nx][ny])
            visited[nx][ny] = 0

dx = [1, 0] # 하, 우
dy = [0, 1]
T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = float('inf')
    dfs(0, 0, data[0][0])
    print("#{} {}".format(test_case + 1, ans))

# T = int(input())
# dx = [1, 0]
# dy = [0, 1]
# def mydfs(x, y):
#     global cost, Min
#     if Min <= cost:
#         return
#     if x == n - 1 and y == n - 1:
#         Min = min(Min, cost)
#         return
#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             cost += graph[nx][ny]
#             mydfs(nx, ny)
#             cost -= graph[nx][ny]
#
# for case in range(1, T + 1):
#     n = int(input())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     Min = 10000
#     cost = graph[0][0]
#     mydfs(0, 0)
#     print("#{} {}".format(case, Min))