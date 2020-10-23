import sys
sys.stdin = open("4340_input.txt", "r")

# dx = [1, 0, - 1, 0]  # 회전; 하, 우, 상, 좌
# dy = [0, 1, 0, - 1]
#
#
# def dfs(x, y, d, cnt):  # 행, 열, 방향, 횟수
#     global ans
#     nx = x + dx[d]
#     ny = y + dy[d]
#
#     if nx == ny == N - 1:
#         if (data[nx][ny] <= 2 and d == 1) or (data[nx][ny] > 3 and d == 0):
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
dx = [1, 0, - 1, 0]  # 회전; 하, 우, 상, 좌
dy = [0, 1, 0, - 1]


def dfs(x, y, d, cnt):  # 행, 열, 방향, 횟수
    global ans
    nx = x + dx[d]
    ny = y + dy[d]

    if nx == ny == N - 1:
        if (data[nx][ny] <= 2 and d == 1) or (data[nx][ny] > 3 and d == 0):
            if ans > cnt:
                ans = cnt
        return

    if 0 <= nx < N and 0 <= ny < N:
        if not visited[nx][ny] and data[nx][ny]:
            visited[nx][ny] = 1
            if data[nx][ny] <= 2:  # 직선
                dfs(nx, ny, d, cnt + 1)  # 직선이면 방향전환 못 함.
            else:  # 곡선
                dfs(nx, ny, (d + 1) % 4, cnt + 1)
                dfs(nx, ny, (d + 3) % 4, cnt + 1)
            visited[nx][ny] = 0


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]  # 방문 check
    ans = float('inf')

    dfs(0, 0, 1 if data[0][0] <= 2 else 0, 0)
    print(f"#{test_case + 1} {ans + 2}")
    # print("#{} {}".format(test_case + 1, ans + 2))
