import sys
sys.stdin = open("1949_input.txt", "r")


def dfs(x, y, height, chance, count):
    global N, K, mat
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N): continue
        if visited[nx][ny]: continue
        if data[nx][ny] >= height:
            if data[nx][ny] - K >= height: continue
            if chance == 0: continue
            visited[nx][ny] = 1
            dfs(nx, ny, data[x][y] - 1, 0, count + 1)
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
    max_height, mat = 0, 0
    for i in range(N):
        max_height = max(max_height, max(data[i]))

    for i in range(N):
        for j in range(N):
            if data[i][j] == max_height:
                visited[i][j] = 1
                dfs(i, j, max_height, 1, 1)
                visited[i][j] = 0
    print("#{} {}".format(test_case + 1, mat))