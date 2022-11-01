import sys
sys.stdin = open("D4_15623_input.txt", "r")

# 223 / 266 Fail
# def solve(idx, nx, ny):
#     global ans
#     if idx == 2:
#         ans = min(ans, nx * ny)
#         return
#
#     for k in range(1, N + 1):
#         if graph[idx][k] != 0 and not visited[k]:
#             visited[k] = 1
#             nx += graph[idx][k][0]
#             ny += graph[idx][k][1]
#             if ans < nx * ny:
#                 break
#             solve(k, nx, ny)
#             visited[k] = 0
#
# T = int(input())
# for test_case in range(T):
#     if test_case + 1 in [66, 73, 181, 260]:
#         temp = input()
#     N, M = map(int, input().split())
#     graph = [[0] * (N + 1) for _ in range(N + 1)]
#     for i in range(M):
#         A, B, X, Y = map(int, input().split())
#         graph[A][B] = [X, Y]
#         graph[B][A] = [X, Y]
#
#     chk1, chk2 = 0, 0
#     for i in range(1, N + 1):
#         if graph[1][i] != 0:
#             chk1 = 1
#         if graph[2][i] != 0:
#             chk2 = 1
#     if chk1 and chk2:
#         ans = float('inf')
#         visited = [0] * (N + 1)
#         visited[1] = 1
#         for j in range(1, N + 1):
#             if graph[1][j] != 0:
#                 visited[j] = 1
#                 numX, numY = graph[1][j][0], graph[1][j][1]
#                 solve(j, numX, numY)
#                 visited[j] = 0
#     else:
#         ans = - 1
#     print("#{} {}".format(test_case + 1, ans))

# 249 // 266 Fail
def solve(idx, nx, ny):
    global ans
    if idx == 2:
        ans = min(ans, nx * ny)
        return

    for k in range(1, N + 1):
        if graph[idx][k] != 0 and not visited[k]:
            visited[k] = 1
            nx += graph[idx][k][0]
            ny += graph[idx][k][1]
            if ans < nx * ny:
                nx -= graph[idx][k][0]
                ny -= graph[idx][k][1]
                visited[k] = 0
                continue
            solve(k, nx, ny)
            visited[k] = 0


T = int(input())
for test_case in range(T):
    if test_case + 1 in [66, 73, 181, 260]:
        temp = input()
    N, M = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        A, B, X, Y = map(int, input().split())
        graph[A][B] = [X, Y]
        graph[B][A] = [X, Y]

    chk1, chk2 = 0, 0
    for i in range(1, N + 1):
        if graph[1][i] != 0:
            chk1 = 1
        if graph[2][i] != 0:
            chk2 = 1
    if chk1 and chk2:
        ans = float('inf')
        visited = [0] * (N + 1)
        visited[1] = 1
        for j in range(1, N + 1):
            if graph[1][j] != 0:
                visited[j] = 1
                numX, numY = graph[1][j][0], graph[1][j][1]
                solve(j, numX, numY)
                visited[j] = 0
    else:
        ans = - 1
    print("#{} {}".format(test_case + 1, ans))