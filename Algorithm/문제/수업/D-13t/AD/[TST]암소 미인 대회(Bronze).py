import sys
sys.stdin = open("[TST]암소 미인 대회(Bronze)_input.txt", "r")

def BFS(x, y):
    t = []
    Q = []
    Q.append([x, y])
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]  # 상 하 좌 우

    while Q:
        x, y = Q.pop(0)
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if visited[nx][ny] == 0 and data[nx][ny] == 'X':
                visited[nx][ny] = 1
                Q.append([nx, ny])
            if data[nx][ny] == '.':
                count += 1
        if count > 0:
            t.append([x, y])
    return t

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
flag = 0

for i in range(N):
    for j in range(M):
        if flag == 0 and data[i][j] == 'X' and visited[i][j] == 0:
            cow_1 = BFS(i, j)
            flag = 1
        if flag == 1 and data[i][j] == 'X' and visited[i][j] == 0:
            cow_2 = BFS(i, j)

minn = float('inf')
for i in range(len(cow_1)):
    for j in range(len(cow_2)):
        answer = abs(cow_1[i][0] - cow_2[j][0]) + abs(cow_1[i][1] - cow_2[j][1]) - 1
        if answer < minn:
            minn = answer
print(minn)