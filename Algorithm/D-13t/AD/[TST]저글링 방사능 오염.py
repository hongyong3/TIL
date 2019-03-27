import sys
sys.stdin = open("[TST]저글링 방사능 오염_input.txt", "r")


def BFS(x, y):
    Q = []
    Q.append((x, y))
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]  # 상 하 좌 우

    while len(Q) > 0:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=  0 and nx <  M - 1 and ny >= 0 and ny < N - 1:
                if data[nx][ny] == 1 and visited[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

M, N = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
r, c = map(int, input().split())
visited = [[0] * M for _ in range(N)]
count, ans = 0, -1

BFS(r-1, c-1)

for i in range(M):
    for j in range(N):
        if visited[j][i] > ans:
            ans = visited[j][i]
        elif data[j][i] == 1 and visited[j][i] == 0:
            count += 1

print(ans + 2)
print(count)