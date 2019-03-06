def scan(r, c):
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]    # 상 하 좌 우 좌상 좌하 우상 우하
    dc = [0, 0, -1, 1, -1, -1, 1, 1]    # 상 하 좌 우 좌상 좌하 우상 우하
    count = 0
    for k in range(8):
        for dep in range(1,N):
            new_r = r + dr[k] * dep
            new_c = c + dc[k] * dep
            if new_r >= N or new_r < 0 or new_c >= N or new_c < 0 or data[new_r][new_c] < 2:
                break
            elif data[new_r][new_c] == 2:
                data[new_r][new_c] = 9
                count += 1
    return count

import sys
sys.stdin = open("사냥꾼_input.txt", "r")
N = int(input())
data = [list(map(int, input())) for _ in range(N)]
ans = 0
# 사냥꾼 위치
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            ans += scan(i, j)
print(ans)