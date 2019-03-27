import sys
sys.stdin = open("[PY-TST]토마토(고)_input.txt", "r")

def BFS():
    global count
    Q =  tomato

    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]  # 상 하 좌 우

    while len(Q):
        cnt = 0
        q = Q.pop(0)

        for i in range(4):
            x = q[0] + dx[i]
            y = q[1] + dy[i]
            if x >= 0 and x < N and y >= 0 and y < M and data[x][y] == 0:
                data[x][y] = data[q[0]][q[1]] + 1
                Q.append([x, y])
            else:
                cnt += 1

        if cnt == 4:
            if count < data[q[0]][q[1]] - 1:
                count = data[q[0]][q[1]] - 1


M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
count = 0
flag = 1
tomato = [[i, j] for i in range(N) for j in range(M) if data[i][j] == 1]
print(tomato)

BFS()

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            flag = 0
            break
if flag:
    print(count)
else:
    print(-1)