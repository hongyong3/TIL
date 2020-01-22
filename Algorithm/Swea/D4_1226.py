import sys
sys.stdin = open("D4_1226_input.txt", "r")

dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]
def bfs(x, y):
    visited[x][y] = 1
    q.append((x, y))
    while q:
        x, y, = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if data[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
            if data[nx][ny] == 3:
                return 1
    return 0

for test_case in range(10):
    N = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    q = []

    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                print("#{} {}".format(test_case + 1, bfs(i, j)))
                break