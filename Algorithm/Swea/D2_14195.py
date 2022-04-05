import sys
sys.stdin = open("D2_14195_input.txt", "r")

from collections import deque
dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def bfs(x, y, val):
    global ans
    q = deque()
    q.append((x, y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == val:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    if ans < cnt:
        ans = cnt

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    Acnt, Bcnt, ans = 0, 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '_':
                if not visited[i][j]:
                    visited[i][j] = 1
            else:
                if not visited[i][j]:
                    visited[i][j] = 1
                    if arr[i][j] == 'A':
                        bfs(i, j, 'A')
                        Acnt += 1
                    else:
                        bfs(i, j, 'B')
                        Bcnt += 1

    print("#{} {} {} {}".format(test_case + 1, Acnt, Bcnt, ans))