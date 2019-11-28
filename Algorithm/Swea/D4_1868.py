import sys
sys.stdin = open("D4_1868_input.txt", "r")

dx = [- 1, 1, 0, 0, - 1, - 1, 1, 1]     # 상 하 좌 우 좌상 우상 좌하 우하
dy = [0, 0, - 1, 1, - 1, 1, - 1, 1]

def notMine(q):
    x, y = q
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if data[nx][ny] == '*':
            mine += 1
            continue

    if mine == 0:
        for i in range(8):
            



def dfs(x, y):
    global mine
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        # 만약 주변에 지뢰가 있는 경우
        if data[nx][ny] == '*':
            mine += 1
            continue
    if mine == 0:
        q.append(x, y)
        notMine(q)


T = int(input())
for test_case in range(1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    mine, count = 0, float('inf')
    visited = [[0] * (N) for _ in range(N)]
    q = []
    for x in range(N):
        for y in range(N):
            if data[x][y] == '.' and visited[x][y] == 0:
                dfs(x, y)