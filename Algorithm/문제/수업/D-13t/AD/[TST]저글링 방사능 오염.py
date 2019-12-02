import sys
sys.stdin = open("[TST]저글링 방사능 오염_input.txt", "r")


def isWall(x, y):
    if x < 0 or x > N - 1: return True
    if y < 0 or y > M - 1: return True
    return False

def BFS(x, y):
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]  # 상 하 좌 우

    Q = []
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isWall(nx, ny):
                if data[nx][ny] == 1 and visited[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

M, N = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
r, c = map(int, input().split())
ans = -1
count = 0

BFS(c-1, r-1)

for i in range(N):
    for j in range(M):
        if visited[i][j] > ans:
            ans = visited[i][j]
        if data[i][j] == 1 and visited[i][j] == 0:
            count += 1

print(ans + 2)
print(count)

# def BFS():
#     que = []
#     dr = (-1, 1, 0, 0)  # 상 하 좌 우
#     dc = (0, 0, -1, 1)  # 상 하 좌 우
#     que.append((sr, sc, 3))
#     arr[sr][sc] = 0 # 맵에 방문 표시
#     while que:
#         r, c, time = que.pop(0) # 2) 큐에서 data 읽기(현재좌표)
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr < 0 or nr >= R or nc < 0 or nc >= C:
#                 continue    # 맵의 범위를 벗어나면 스킵
#             if arr[nr][nc] == 1: # 저글링이면
#                 que.append((nr, nc, time + 1))
#                 arr[nr][nc] = 0    # 맵에 방문표시
#     return time # 4) 큐가 빈상태(더이상 없앨 저글링이 없는 경우)
#
# C, R = map(int, input().split())
# arr = []
# for i in range(R):
#     arr.append(list(map(int, input())))
# sc, sr = map(int, input().split())
# visited = [[0] * C for _ in range(R)]
# sc -= 1; sr -= 1;
#
# print(BFS())
# print()