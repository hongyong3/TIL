import sys
sys.stdin = open("5656_input.txt" ,"r")
from itertools import product

dx = [0, 0, - 1, 1] # 상 하 좌 우
dy = [- 1, 1, 0, 0]

def block(i, j, k):
    q = [(i, j, k)]
    copyData[i][j] = 0
    while q:
        x, y, z = q.pop()
        for i in range(4):
            bomb = 0
            while bomb < z:
                nx = x + dx[i] * bomb
                ny = y + dy[i] * bomb
                if 0 <= nx < H and 0 <= ny < W:
                    if copyData[nx][ny]:
                        q.append((nx, ny, copyData[nx][ny]))
                        copyData[nx][ny] = 0
                bomb += 1

def gravity():
    for y in range(W):
        bottom = H - 1
        for x in range(H - 1, - 1, - 1):
            if bottom != x:
                if copyData[bottom][y]:
                    bottom -= 1
                elif copyData[x][y]:
                    copyData[bottom][y], copyData[x][y] = copyData[x][y], 0
                    bottom -= 1

def start(w):
    for y in w:
        for x in range(H):
            if copyData[x][y]:
                block(x, y, copyData[x][y])
                gravity()
                break

T = int(input())
for test_case in range(T):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')

    for i in product(range(W), repeat = N):
        copyData = [data[j][:] for j in range(H)]
        start(i)
        ans = 0
        for j in copyData:
            ans += len(j) - j.count(0)
        ans = min(ans, ans)
        if not ans:
            break
    print("#{} {}".format(test_case + 1, ans))

# test = [[0, 1, 2, 3, 4, 0, 0], [0, 1, 2, 3]]
# cnt = 0
# for i in test:
#     cnt += len(i) - i.count(0)
# print(cnt)