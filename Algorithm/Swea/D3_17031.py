import sys
sys.stdin = open("D3_17031_input.txt", "r")

from collections import deque
dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                temp = 0
                if arr[nx][ny] > arr[x][y]:
                    temp = arr[nx][ny] - arr[x][y]
                if visited[nx][ny] > visited[x][y] + temp + 1:
                    visited[nx][ny] = visited[x][y] + temp + 1
                    q.append([nx, ny])
    return visited[- 1][- 1]

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    ans = bfs()
    print("#{} {}".format(test_case + 1, ans))