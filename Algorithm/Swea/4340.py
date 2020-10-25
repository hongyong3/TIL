import sys
sys.stdin = open("4340_input.txt", "r")

# dx = [1, 0, - 1, 0]  # 회전; 하, 우, 상, 좌
# dy = [0, 1, 0, - 1]
#
# def dfs(x, y, d, cnt):  # 행, 열, 방향, 횟수
#     global ans
#     nx = x + dx[d]
#     ny = y + dy[d]
#
#     if nx == ny == N - 1:
#         if (data[nx][ny] <= 2 and d == 1) or (data[nx][ny] > 2 and d == 0):
#             if ans > cnt:
#                 ans = cnt
#         return
#
#     if 0 <= nx < N and 0 <= ny < N:
#         if not visited[nx][ny] and data[nx][ny]:
#             visited[nx][ny] = 1
#             if data[nx][ny] <= 2:  # 직선
#                 dfs(nx, ny, d, cnt + 1)  # 직선이면 방향전환 못 함.
#             else:  # 곡선
#                 dfs(nx, ny, (d + 1) % 4, cnt + 1)
#                 dfs(nx, ny, (d + 3) % 4, cnt + 1)
#             visited[nx][ny] = 0
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]  # 방문 check
#     ans = float('inf')
#
#     dfs(0, 0, 1 if data[0][0] <= 2 else 0, 0)
#     print(f"#{test_case + 1} {ans + 2}")

# 22 / 50 runtime error
# 출발점에서 시작
# dx = [1, 0, - 1, 0]  # 회전; 하, 우, 상, 좌
# dy = [0, 1, 0, - 1]
#
# def dfs(x, y, d, cnt):  # 행, 열, 방향, 횟수
#     global ans
#     nx = x + dx[d]
#     ny = y + dy[d]
#
#     if nx == ny == N - 1:
#         if (data[nx][ny] <= 2 and d == 1) or (data[nx][ny] > 2 and d == 0):
#             if ans > cnt:
#                 ans = cnt
#         return
#
#     if 0 <= nx < N and 0 <= ny < N:
#         if not visited[nx][ny] and data[nx][ny]:
#             visited[nx][ny] = 1
#             if data[nx][ny] <= 2:  # 직선
#                 dfs(nx, ny, d, cnt + 1)  # 직선이면 방향전환 못 함.
#             else:  # 곡선
#                 dfs(nx, ny, (d + 1) % 4, cnt + 1)
#                 dfs(nx, ny, (d + 3) % 4, cnt + 1)
#             visited[nx][ny] = 0
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]  # 방문 check
#     ans = float('inf')
#
#     dfs(0, 0, 1 if data[0][0] <= 2 else 0, 0)
#     print(f"#{test_case + 1} {ans + 2}")

# 28 / 50 runtime error
# 도착점에서 시작
# dx = [1, 0, - 1, 0]  # 회전; 하, 우, 상, 좌
# dy = [0, 1, 0, - 1]
#
# def solve(x, y, d, cnt):
#     global ans
#     nx = x + dx[d]
#     ny = y + dy[d]
#
#     if nx == ny == 0:
#         if (data[nx][ny] > 2 and d == 2) or (data[nx][ny] <= 2 and d == 3):
#             ans = min(ans, cnt)
#             return
#
#     if 0 <= nx < N and 0 <= ny < N:
#         if not visited[nx][ny] and data[nx][ny]:
#             visited[nx][ny] = 1
#             if data[nx][ny] <= 2:
#                 solve(nx, ny, d, cnt + 1)
#             else:
#                 solve(nx, ny, (d + 1) % 4, cnt + 1)
#                 solve(nx, ny, (d + 3) % 4, cnt + 1)
#             visited[nx][ny] = 0
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     ans = float('inf')
#
#     solve(N - 1, N - 1, 2 if data[N - 1][N - 1] > 2 else 3, 0)
#     print(f"#{test_case + 1} {ans + 2}")

def solve(px, py, x, y, cnt):
    global ans, ex, ey
    if x == ex and y == ey:
        ans = min(ans, cnt)
        return

    if not (0 <= x < N and 0 <= y < N):
        return

    if visited[y][x] == 1:
        return
    visited[y][x] = 1

    if px == x and py == y - 1:
        if cnt < depth[y][x][0]:
            depth[y][x][0] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x, y + 1, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x - 1, y, cnt + 1)
                solve(x, y, x + 1, y, cnt + 1)

    elif px == x and py == y + 1:
        if cnt < depth[y][x][1]:
            depth[y][x][1] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x, y - 1, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x + 1, y, cnt + 1)
                solve(x, y, x - 1, y, cnt + 1)

    elif px == x - 1 and py == y:
        if cnt < depth[y][x][2]:
            depth[y][x][2] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x + 1, y, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x, y + 1, cnt + 1)
                solve(x, y, x, y - 1, cnt + 1)

    else:
        if cnt < depth[y][x][3]:
            depth[y][x][3] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x - 1, y, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x, y + 1, cnt + 1)
                solve(x, y, x, y - 1, cnt + 1)
    visited[y][x] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')

    for i in range(2):
        depth = [[[N * N] * 4 for _ in range(N)] for _ in range(N)]
        visited = [[0] * N for _ in range(N)]
        if not i:
            ex, ey = N, N - 1
            solve(- 1, 0, 0, 0, 0)
        else:
            ex, ey = - 1, 0
            solve(N, N - 1, N - 1, N - 1, 0)
    print(f"#{test_case + 1} {ans}")