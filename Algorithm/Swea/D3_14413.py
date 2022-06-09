import sys
sys.stdin = open("D3_14413_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def dfs(x, y, v):
    global ans
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            if v == '#':
                if arr[nx][ny] == '?':
                    arr[nx][ny] = '.'
                elif arr[nx][ny] == '#':
                    ans = 'impossible'
                    return
            else:
                if arr[nx][ny] == '?':
                    arr[nx][ny] = '#'
                elif arr[nx][ny] == '.':
                    ans = 'impossible'
                    return

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 'possible'

    for i in range(N):
        for j in range(M):
            if arr[i][j] in '#.':
                visited[i][j] = 1
                val = arr[i][j]
                dfs(i, j, val)

    print("#{} {}".format(test_case + 1, ans))