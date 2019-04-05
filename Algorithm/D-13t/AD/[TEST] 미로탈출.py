import sys
sys.stdin = open("[TEST] 미로탈출_input.txt", "r")

# def BFS(x, y, boom, count):
#     Q = []
#     Q.append([x, y, boom, count])
#     dx = [-1, 1, 0, 0]  # 상 하 좌 우
#     dy = [0, 0, -1, 1]  # 상 하 좌 우
#     visited[0][x][y] = 1
#     while Q:
#         x, y, boom, count = Q.pop(0)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
#             if data[nx][ny] == 1: continue  # 벽이면
#             if data[nx][ny] == 0:
#                 if visited[boom][nx][ny]: continue
#                 Q.append((nx, ny, boom, count + 1))
#                 visited[boom][nx][ny] = 1
#             elif data[nx][ny] == 2:
#                 if boom < 3 and not visited[boom + 1][nx][ny]:
#                     Q.append((nx, ny, boom + 1, count + 1))
#                     visited[boom+1][nx][ny]  = 1
#
# R, C = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(C)]
# visited = [[0]* C for _ in range(R) for _ in range(4)]
# for i in range(R-1):
#     for j in range(C-1):
#         if data[i][j] == 3:
#             x, y = i, j
# BFS(x, y, 0, 0)


def iswall(y, x):
    if y < 0 or y >= Y: return True
    if x < 0 or x >= X: return True
    if maps[y][x] == 1: return True
    return False


def escape():
    global result
    que = [[sy, sx, 3, 0]]
    visit[3][sy][sx] = 1

    while que:
        y, x, bomb, turn = que.pop(0)

        for i in range(4):

            ny, nx = y + dy[i], x + dx[i]

            if iswall(ny, nx): continue
            if visit[bomb][ny][nx]: continue

            if maps[ny][nx] == 4:
                result = turn + 1
                return

            if maps[ny][nx] == 0:
                que.append([ny, nx, bomb, turn+1])
                visit[bomb][ny][nx] = 1

            if maps[ny][nx] == 2 and bomb:
                que.append([ny, nx, bomb-1, turn+1])
                visit[bomb-1][ny][nx] = 1



Y, X = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(Y)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for y in range(Y):
    for x in range(X):
        if maps[y][x] == 3:
            sy, sx = y, x
        if maps[y][x] == 4:
            ey, ex = y, x

visit = [[[0 for _ in range(X)] for _ in range(Y)] for _ in range(4)]
result = -1
escape()
print(result)