import sys
sys.stdin = open("1953_input.txt", "r")

up = [1, 2, 4, 7]
down = [1, 2, 5, 6]
left = [1, 3, 6, 7]
right = [1, 3, 4, 5]
dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]  # 상 하 좌 우​

T = int(input())
for test_case in range(T):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    mat = 0
    q = [(R, C, 1)]
    visited[R][C] = 1
    while q:

        r, c, t = q.pop(0)
        if t + 1 <= L:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < M): continue
                if i == 0:  # 상
                    if data[r][c] in up and data[nr][nc] in down:
                        if visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc, t + 1))
                if i == 1:  # 하
                    if data[r][c] in down and data[nr][nc] in up:
                        if visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc, t + 1))
                if i == 2:  # 좌
                    if data[r][c] in left and data[nr][nc] in right:
                        if visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc, t + 1))
                if i == 3:  # 우
                    if data[r][c] in right and data[nr][nc] in left:
                        if visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc, t + 1))
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                mat += 1
    print("#{} {}".format(test_case + 1, mat))