import sys
sys.stdin = open("[PY-TST]토마토(고)_input.txt", "r")
M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            x, y = i, j