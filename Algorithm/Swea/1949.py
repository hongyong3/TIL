import sys
sys.stdin = open("1949_input.txt", "r")

# def dfs(height, x, y, chance, count):
#     global N, K, ans
#     dx = [-1, 1, 0, 0]  # 상 하 좌 우
#     dy = [0, 0, -1, 1]  # 상 하 좌 우
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if not (0 <= nx < N and 0 <= ny < N): continue
#         if visited[nx][ny]: continue        # 체크라면
#         if data[nx][ny] >= height:           # 이전 경로와 높이가 같거나 크다면
#             if chance == 0: continue
#             if data[nx][ny] - K >= height: continue  # chance가 없거나 공사를 해도 이전 경로와 높이가 같거나 크다면
#             visited[nx][ny] = 1
#             dfs(data[nx][ny] - 1, nx, ny, 0, count + 1)
#             visited[nx][ny] = 0
#             continue
#         visited[nx][ny] = 1
#         dfs(data[nx][ny], nx, ny, chance, count + 1)
#         visited[nx][ny] = 0
#     ans = max(ans, count)
#
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     max_height, ans = 0, 0  # 최대높이, 등산로 길이
#
#     for i in range(N):  # 최대 높이 찾기
#         max_height = max(max_height, max(data[i]))
#
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == max_height:
#                 visited[i][j] = 1   # 체크
#                 dfs(max_height, i, j, 1, 1)    # 높이, x, y, chance, count
#                 visited[i][j] = 0
#     print("#{} {}".format(test_case + 1, ans))

def dfs(x, y, height, chance, count):
    global N, K, ans
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if visited[nx][ny]:
            continue
        if data[nx][ny] >= height:
            if data[nx][ny] - K >= height:
                continue
            if chance == 0:
                continue
            visited[nx][ny] = 1
            dfs(nx, ny, data[nx][ny] - 1, 0, count + 1)
            visited[nx][ny] = 0
            continue
        visited[nx][ny] = 1
        dfs(nx, ny, data[nx][ny], chance, count + 1)
        visited[nx][ny] = 0
    ans = max(ans, count)

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_height, ans = 0, 0
    for i in range(N):
        max_height = max(max_height, max(data[i]))

    for i in range(N):
        for j in range(N):
            if data[i][j] == max_height:
                visited[i][j] = 1
                dfs(i, j, max_height, 1, 1)
                visited[i][j] = 0
    print("#{} {}".format(test_case + 1, ans))