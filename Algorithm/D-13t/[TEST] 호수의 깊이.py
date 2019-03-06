def lake(r, c):
    dr = [-1, 1, 0, 0]  # 상 하 좌 우
    dc = [0, 0, -1, 1]  # 상 하 좌 우
    for dep in range(1, N): # 1부터 시작한 이유는 가장자리는 육지라서
        for i in range(4):
            if data[r + dr[i] * dep][c + dc[i] * dep] == 0:
                return dep

import sys
sys.stdin = open("호수의 깊이_input.txt", "r")
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 육지와의 거리구하기
for i in range(1,N):
    for j in range(1,N):
        if data[i][j] != 0: # 호수 위치
            data[i][j] = lake(i,j)

# 거리 count
for i in range(N):
    for j in range(N):
        ans += data[i][j]

print(ans)