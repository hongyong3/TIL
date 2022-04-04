import sys
sys.stdin = open("D2_14195_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]
def dfs(x, y, cnt):
    for i in

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    Acnt, Bcnt, ans = 0, 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] != '_' and not visited[i][j]:
                if arr[i][j] == 'A':
                    Acnt += 1
