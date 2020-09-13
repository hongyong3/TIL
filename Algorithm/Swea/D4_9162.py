import sys
sys.stdin = open("D4_9162_input.txt", "r")

dx = [0, - 1, 0, 1] # 상 좌 하 우
dy = [- 1, 0, 1, 0]

dice = [
    [3, 4, 1, 2],
    [0, 1, 5, 1],
    [2, 0, 2, 5],
    [5, 3, 0, 3],
    [4, 5, 4, 0],
    [1, 2, 3, 4],
]

def dfs(x, y, deep, loc):
    global mat
    if data[y][x] == 3:
        if not loc:
            ans = min(ans, deep)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and data[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs(nx, ny, deep + 1, dice[loc][i])
            visited[ny][nx] = 0

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    mat = float('inf')

    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                visited[i][j] = 1
                dfs(j, i, 0, 0)
                break

    if mat == float('inf'):
        mat = - 1
    print('#{} {}'.format(test_case + 1, mat))